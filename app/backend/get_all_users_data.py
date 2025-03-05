from fastapi import APIRouter, Query
from sqlalchemy import select

from app.core import async_session_maker, UsersModel

get_all_users_data_router = APIRouter()


@get_all_users_data_router.get(path="/get_all_users_data", status_code=200)
async def get_all_users_data(
    page: int = Query(ge=1),
    limit: int = Query(3, ge=1)
):
    async with async_session_maker() as session:
        # Вычисляем смещение для пагинации
        offset = (page - 1) * limit

        # Выполняем запрос с пагинацией
        result = await session.execute(
            select(UsersModel)
            .offset(offset)
            .limit(limit)
        )

        response = result.scalars().all()
        return {
            "users": [
                {
                    "username": user.username,
                    "age": user.age,
                    "hobbies": user.hobbies,
                    "bio": user.bio,
                    "telegram": user.telegram,
                    "email": user.email,
                    "phone": user.phone,
                    "other": user.other,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                }
                for user in response
                # list компрэхэншоны
            ],

            "page": page,
            "limit": limit,
            "total": len(response)
        }
