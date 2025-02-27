from fastapi import APIRouter
from sqlalchemy import select, desc

from app.core import async_session_maker, AuthModel


get_latest_username_router = APIRouter()


@get_latest_username_router.get(path="/get_latest_username", status_code=200)
async def get_latest_username():
    async with async_session_maker() as session:
        result = await session.execute(
            select(AuthModel.username).order_by(
                desc(AuthModel.auth_id)
            ).limit(1)
        )
        response = result.scalars().first()

        return response
