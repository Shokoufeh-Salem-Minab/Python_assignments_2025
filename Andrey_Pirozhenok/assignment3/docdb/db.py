"""
A production-grade document-based database that does not waste disc space or processor cycles
and most definetly does not contain any security vulnerabilities.
Basicaly redis but better. (And slower, less powerful, less secure...)

A database contains of multiple tables.
Each table contains keyed documents.
Documents are JSON values.
"""

from typing import Tuple, Callable
import os
import os.path
import shutil
import json


JSONable = str | int | float | bool | None | dict[str, "JSONable"] | list["JSONable"]


class Connection:
    def __init__(self, path: str):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def table_list(self) -> list[str]:
        return list(
            map(
                lambda entry: entry.name,
                filter(
                    lambda entry: entry.is_dir(),
                    os.scandir(self.path),
                ),
            )
        )

    def table_create(self, table: str) -> None:
        path = self._safe_join(table)
        if os.path.exists(path):
            # Yes, I know that should subtype an exception, but I cannot be bothered to do so.
            raise Exception("table already exists")
        os.mkdir(path)

    def table_create_if_not_exists(self, table: str) -> None:
        path = self._safe_join(table)
        if not os.path.exists(path):
            os.mkdir(path)

    def table_drop(self, table: str) -> None:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")
        # So, yes, this is scary, huh
        shutil.rmtree(path)

    def data_entries(self, table: str) -> list[Tuple[str, JSONable]]:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")

        res = []

        for entry in os.scandir(path):
            if entry.is_dir():
                continue
            res.append((entry.name, _read_file(entry.path)))

        return res

    # Yes, this is a go-style API, but I prefer to not use exceptions for such cases.
    def data_lookup(self, table: str, key: str) -> Tuple[JSONable, bool]:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")

        path = self._safe_join(table, key)
        if not os.path.exists(path):
            return (None, False)

        return (_read_file(path), True)

    def data_insert(self, table: str, key: str, value: JSONable) -> None:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")

        path = self._safe_join(table, key)
        if os.path.exists(path):
            raise Exception("key already exists")

        _write_file(path, value)

    def data_upsert(self, table: str, key: str, value: JSONable) -> None:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")

        path = self._safe_join(table, key)
        _write_file(path, value)

    def data_map(
        self, table: str, key: str, mapper: Callable[[JSONable], JSONable]
    ) -> None:
        path = self._safe_join(table)
        if not os.path.exists(path):
            raise Exception("table does not exist")

        path = self._safe_join(table, key)
        if not os.path.exists(path):
            return

        new_val = mapper(_read_file(path))
        _write_file(path, new_val)

    def _safe_join(self, *args: list[str]) -> str:
        assert len(args) > 0
        return os.path.join(self.path, *map(_validate_ident, args))


_GOOD_CHARS = "01234567890aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ_-"


def is_valid_ident(p: str) -> bool:
    return all(map(lambda c: c in _GOOD_CHARS, p))


def _validate_ident(p: str) -> str:
    assert is_valid_ident(p), f"{p} is not a valid db object name"
    return p


def _read_file(path: str) -> JSONable:
    with open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def _write_file(path: str, value: JSONable) -> None:
    with open(path, "wt", encoding="utf-8") as f:
        json.dump(value, f)
