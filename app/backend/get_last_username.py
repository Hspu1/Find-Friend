from fastapi import HTTPException, APIRouter
from sqlalchemy import select, desc
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, AuthModel


get_latest_username_router = APIRouter()


@get_latest_username_router.get(path="/get_latest_username", status_code=200)
async def get_latest_username():
    async with async_session_maker() as session:
        try:
            result = await session.execute(
                select(AuthModel).order_by(
                    desc(AuthModel.username)).limit(1)
            )

            return result.scalars().first()

        except IntegrityError:
            raise HTTPException(status_code=404)
