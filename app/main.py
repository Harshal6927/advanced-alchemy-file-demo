from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from app.config import alchemy
from app.controllers.note import NoteController

app = Litestar(
    route_handlers=[NoteController],
    plugins=[alchemy],
    debug=True,
    openapi_config=OpenAPIConfig(
        title="File Storage Demo",
        version="dev",
        render_plugins=[ScalarRenderPlugin()],
    ),
)
