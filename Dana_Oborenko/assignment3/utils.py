from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Dict, List


def read_lines(file_path: Path) -> List[str]:
    """Read non-empty lines from a text file."""
    text = file_path.read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]


def write_json(file_path: Path, data: Dict[str, Any]) -> None:
    """Write dict data to a JSON file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
