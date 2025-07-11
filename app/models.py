from advanced_alchemy.base import BigIntAuditBase
from advanced_alchemy.types.file_object import FileObject, StoredObject
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class NoteModel(BigIntAuditBase):
    __tablename__ = "notes"

    title: Mapped[str]
    body: Mapped[str | None]

    # -----------------
    # ORM Relationships
    # -----------------

    files: Mapped[list["FileModel"] | None] = relationship()


class FileModel(BigIntAuditBase):
    __tablename__ = "files"

    blob: Mapped[FileObject] = mapped_column(
        StoredObject(backend="note_files"),
        nullable=True,
    )
    note_id: Mapped[int] = mapped_column(ForeignKey("notes.id", ondelete="CASCADE"))

    # -----------------
    # ORM Relationships
    # -----------------

    note: Mapped[NoteModel] = relationship(back_populates="files")
