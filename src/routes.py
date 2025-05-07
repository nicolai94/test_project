from litestar import Router
from src.service import UserController

user_router = Router(
    path="/users",
    route_handlers=[UserController]
)
