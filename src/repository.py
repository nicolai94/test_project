from typing import Sequence

from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError

from src.models import User
from src.schemas import UserCreate
from litestar.plugins.sqlalchemy import repository


class UserRepository(repository.SQLAlchemyAsyncRepository[User]):
    model_type = User

    async def get_user_by_id(self, user_id: int):
        stmt = select(self.model_type).where(self.model_type.id == user_id)
        result = await self.session.execute(stmt)

        return result.scalars().first()

    async def create_user(self, data: UserCreate) -> User:
        user = User(**data.model_dump())
        self.session.add(user)
        try:
            await self.session.commit()
            await self.session.refresh(user)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e

        return user

    async def get_users(self) -> Sequence[User]:
        stmt = select(self.model_type)
        result = await self.session.execute(stmt)

        return result.scalars().all()

    async def delete_user(self, user_id: int) -> None:
        stmt = select(self.model_type).where(self.model_type.id == user_id)
        result = await self.session.execute(stmt)

        user = result.scalars().first()

        await self.session.delete(user)

        try:
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e

    async def update_user(self, user_id: int, data: dict) -> User | None:
        stmt = (
            update(self.model_type)
            .where(self.model_type.id == user_id)
            .values(**data)
            .returning(self.model_type)
        )
        result = await self.session.execute(stmt)

        try:
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise e

        return result.scalars().first()
