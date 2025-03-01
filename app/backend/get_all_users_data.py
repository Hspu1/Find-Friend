from fastapi import APIRouter
from sqlalchemy import select

from app.core import async_session_maker, UsersModel

get_all_users_data_router = APIRouter()


@get_all_users_data_router.get(path="/get_all_users_data", status_code=200)
async def get_all_users_data():
    async with async_session_maker() as session:
        result = await session.execute(select(UsersModel))

        response = result.scalars().all()
        print(response)
