from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import (
    SQLAlchemyAsyncRepositoryService,
)

from app.models import FileModel, NoteModel


class NoteService(SQLAlchemyAsyncRepositoryService[NoteModel]):
    class NoteRepository(SQLAlchemyAsyncRepository[NoteModel]):
        model_type = NoteModel

    repository_type = NoteRepository


class FileService(SQLAlchemyAsyncRepositoryService[FileModel]):
    class FileRepository(SQLAlchemyAsyncRepository[FileModel]):
        model_type = FileModel

    repository_type = FileRepository
