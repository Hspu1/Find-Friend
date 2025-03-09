import bcrypt
from fastapi import Form, APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, AuthModel


submit_password_router = APIRouter()


@submit_password_router.post(path="/submit_password", status_code=201)
async def submit_password(username: str = Form(...),
                          password: str = Form(...)):
    async with async_session_maker() as session:
        # Проверяем существование пользователя
        existing_user = await session.execute(
            select(AuthModel).where(AuthModel.username == username)
        )
        if existing_user.scalar():
            raise HTTPException(status_code=409,
                                detail="Username already exists")

        # Создаем нового пользователя
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = AuthModel(
            username=username,
            hashed_psw=hashed_password.decode()
        )
        session.add(new_user)
        await session.commit()
