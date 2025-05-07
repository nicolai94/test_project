from contextlib import asynccontextmanager

from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from src.database import sqlalchemy_plugin
from src.routes import user_router
from litestar_granian import GranianPlugin


@asynccontextmanager
async def lifespan(app: Litestar):
    yield


app = Litestar(
    lifespan=[lifespan],
    route_handlers=[user_router],
    openapi_config=OpenAPIConfig(title="User API", version="1.0.0"),
    plugins=[GranianPlugin(), sqlalchemy_plugin],
    debug=True,
)
