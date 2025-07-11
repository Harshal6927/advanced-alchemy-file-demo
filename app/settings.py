import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from advanced_alchemy.types.file_object import storages
from advanced_alchemy.types.file_object.backends.obstore import ObstoreBackend
from obstore.store import LocalStore
from rich import get_console

console = get_console()


@dataclass
class ObjectStorageSettings:
    def register_storage(self) -> None:
        storages.register_backend(
            ObstoreBackend(
                key="note_files",
                fs=LocalStore(prefix="test_storage", mkdir=True),
            ),
        )


@dataclass
class Settings:
    db_connection_string: str = field(
        default_factory=lambda: os.getenv("DB_CONNECTION_STRING", "sqlite+aiosqlite:///test.sqlite"),
    )
    object_storage: ObjectStorageSettings = field(
        default_factory=ObjectStorageSettings,
    )

    def __post_init__(self) -> None:
        self.object_storage.register_storage()

    @classmethod
    def from_env(cls, dotenv_filename: str) -> "Settings":
        env_file = (
            Path(dotenv_filename) if Path(dotenv_filename).is_absolute() else Path(f"{os.curdir}/{dotenv_filename}")
        )

        if env_file.is_file():
            from dotenv import load_dotenv  # noqa: PLC0415

            console.print(
                f"[yellow]Loading environment configuration from {dotenv_filename}[/]",
                markup=True,
            )

            load_dotenv(env_file, override=True)
        return Settings()


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings.from_env(
        dotenv_filename=".env",
    )
