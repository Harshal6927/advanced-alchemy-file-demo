from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.lib.services import FileService, NoteService


async def provide_note_service(
    db_session: AsyncSession | None = None,
) -> AsyncGenerator[NoteService, None]:
    async with NoteService.new(
        session=db_session,
        error_messages={
            "not_found": "No note found with the given ID.",
        },
    ) as service:
        yield service


async def provide_file_service(
    db_session: AsyncSession | None = None,
) -> AsyncGenerator[FileService, None]:
    async with FileService.new(
        session=db_session,
        error_messages={
            "not_found": "No file found with the given ID.",
        },
    ) as service:
        yield service
