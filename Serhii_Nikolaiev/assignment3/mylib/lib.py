from dataclasses import dataclass
from pathlib import Path

import lz4.frame
from fastcrc import crc32

ALLOWED_COMPRESSION_LEVELS = list(
    range(lz4.frame.COMPRESSIONLEVEL_MIN, lz4.frame.COMPRESSIONLEVEL_MAX + 1)
)


@dataclass
class FileFlags:
    use_lz4: bool
    use_crc32: bool


class MagicBytes:
    USE_LZ4 = b"LZ4"
    DONT_USE_LZ4 = b"FUL"
    USE_CRC = b"CRC"
    DONT_USE_CRC = b"USF"

    MAGIC_BYTES_LENGTH = 6

    @staticmethod
    def get_magic_bytes_length() -> int:
        return MagicBytes.MAGIC_BYTES_LENGTH

    @staticmethod
    def get_magic_bytes(file_flags: FileFlags) -> bytes:
        match (file_flags.use_lz4, file_flags.use_crc32):
            case (True, True):
                return MagicBytes.USE_LZ4 + MagicBytes.USE_CRC
            case (True, False):
                return MagicBytes.USE_LZ4 + MagicBytes.DONT_USE_CRC
            case (False, True):
                return MagicBytes.DONT_USE_LZ4 + MagicBytes.USE_CRC
            case (False, False):
                return MagicBytes.DONT_USE_LZ4 + MagicBytes.DONT_USE_CRC

    @staticmethod
    def parse_magic_bytes(magic_bytes: bytes) -> FileFlags:
        use_lz4: bool
        use_crc32: bool

        assert len(magic_bytes) == MagicBytes.get_magic_bytes_length(), (
            f"Magic bytes mismatch. Expected: {MagicBytes.get_magic_bytes_length()}, received: {len(magic_bytes)}"
        )

        match magic_bytes[0:3]:
            case MagicBytes.USE_LZ4:
                use_lz4 = True
            case MagicBytes.DONT_USE_LZ4:
                use_lz4 = False
            case error:
                raise RuntimeError(f"Invalid magic bytes: {error}")

        match magic_bytes[3:6]:
            case MagicBytes.USE_CRC:
                use_crc32 = True
            case MagicBytes.DONT_USE_CRC:
                use_crc32 = False
            case error:
                raise RuntimeError(f"Invalid magic bytes: {error}")

        return FileFlags(use_lz4, use_crc32)


class File:
    def __init__(self, use_lz4: bool = True, use_crc32: bool = True):
        self.bytes = None
        self.file_flags = FileFlags(use_lz4=use_lz4, use_crc32=use_crc32)
        if self.file_flags.use_lz4:
            self.lz4_level = lz4.frame.COMPRESSIONLEVEL_MINHC
        else:
            self.lz4_level = None

    def set_compression_level(self, level: int):
        if not self.file_flags.use_lz4:
            raise RuntimeError("Compression/Decompression was not enabled")
        if level not in ALLOWED_COMPRESSION_LEVELS:
            raise RuntimeError(
                f"Compression level {level} is not supported. Allowed values: {ALLOWED_COMPRESSION_LEVELS}"
            )
        self.lz4_level = level

    def get_compression_level(self):
        if not self.file_flags.use_lz4:
            raise RuntimeError("Compression/Decompression was not enabled")
        return self.lz4_level

    def get_bytes(self) -> bytes:
        if self.bytes is None:
            raise RuntimeError("Bytes not set.")
        return self.bytes

    def add_bytes(self, bytes_: bytes):
        self.bytes = bytes_

    @staticmethod
    def from_file(file: Path) -> "File":
        try:
            with open(file, "rb") as f:
                data = f.read()
                if len(data) < MagicBytes.get_magic_bytes_length():
                    raise RuntimeError(
                        f"{file} is too small to contain valid magic bytes."
                    )

                file_magic = data[: MagicBytes.get_magic_bytes_length()]
                file_flags = MagicBytes.parse_magic_bytes(file_magic)

                self = File(file_flags.use_lz4, file_flags.use_crc32)

                self.add_bytes(data[MagicBytes.get_magic_bytes_length() :])

                if self.file_flags.use_crc32:
                    crc32_ = self._exclude_crc32()
                    if crc32_ != self._get_crc32():
                        raise RuntimeError("CRC32 mismatch")

                if self.file_flags.use_lz4:
                    self._decompress()
        except FileNotFoundError:
            raise RuntimeError(f"{file} does not exist.")
        except PermissionError:
            raise RuntimeError(f"{file} could not be opened for reading.")
        except IsADirectoryError:
            raise RuntimeError(f"{file} is a directory.")
        except OSError as error:
            raise RuntimeError(f"{file} could not be read: {error}")
        return self

    def write_file(self, file: Path):
        try:
            magic_bytes = MagicBytes.get_magic_bytes(self.file_flags)
            data_to_write = magic_bytes

            if self.file_flags.use_lz4:
                self._compress()

            if self.file_flags.use_crc32:
                data_to_write += self._get_crc32().to_bytes(4)
            data_to_write += self.get_bytes()

            with open(file, "wb") as f:
                f.write(data_to_write)
        except FileNotFoundError:
            raise RuntimeError(f"{file} does not exist.")
        except PermissionError:
            raise RuntimeError(f"{file} could not be opened for writing.")
        except IsADirectoryError:
            raise RuntimeError(f"{file} is a directory.")
        except OSError as error:
            raise RuntimeError(f"{file} could not be written: {error}")

    def _compress(self):
        if not self.file_flags.use_lz4:
            raise RuntimeError("Compression/Decompression was not enabled.")
        # `lz4.frame.compress` contains `content_checksum` param, but it's ignored to add our own checksum
        self.bytes = lz4.frame.compress(self.get_bytes(), self.lz4_level)

    def _decompress(self):
        if not self.file_flags.use_lz4:
            raise RuntimeError("Compression/Decompression was not enabled.")
        self.bytes = lz4.frame.decompress(self.get_bytes())

    def _get_crc32(self) -> int:
        return crc32.bzip2(self.get_bytes())

    def _exclude_crc32(self) -> int:
        crc32_ = self.bytes[0:4]
        self.bytes = self.bytes[4:]
        return int.from_bytes(crc32_)
