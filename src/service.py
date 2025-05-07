from litestar import Controller, post, get, put, delete
from litestar.di import Provide

from src.dependencies import provide_users_repo
from src.repository import UserRepository
from src.schemas import UserCreate, UserUpdate, UserSchema, UserRead, ListUserReadSchema


class UserController(Controller):
    dependencies = {"user_repo": Provide(provide_users_repo)}

    @post()
    async def create_user(self, data: UserCreate, user_repo: UserRepository) -> UserSchema:
        user = await user_repo.create_user(data)

        return UserSchema.model_validate(user, from_attributes=True)

    @get(path="/{user_id:int}")
    async def get_user(self,  user_id: int, user_repo: UserRepository) -> UserRead | None:
        user = await user_repo.get_user_by_id(user_id)

        return UserRead.model_validate(user)

    @get()
    async def list_users(self, user_repo: UserRepository) -> ListUserReadSchema:
        users = await user_repo.get_users()
        result = ListUserReadSchema(users=[UserRead.model_validate(user) for user in users])

        return result

    @put("/{user_id:int}")
    async def update_user(self, user_id: int, data: UserUpdate, user_repo: UserRepository) -> UserSchema | None:
        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        updated_user = await user_repo.update_user(user_id, raw_obj)

        return UserSchema.model_validate(updated_user)

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int, user_repo: UserRepository) -> None:
        await user_repo.delete_user(user_id)

