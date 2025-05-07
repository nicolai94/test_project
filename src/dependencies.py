from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User
from src.repository import UserRepository


async def provide_users_repo(db_session: AsyncSession) -> UserRepository:
    return UserRepository(session=db_session)


async def provide_user_details_repo(db_session: AsyncSession) -> UserRepository:
    return UserRepository(
        statement=select(User),
        session=db_session,
    )