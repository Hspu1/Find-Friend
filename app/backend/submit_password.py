import bcrypt
from fastapi import Form, APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, AuthModel


submit_password_router = APIRouter()


@submit_password_router.post(path="/submit_password", status_code=201)
async def submit_password(username: str = Form(...), password: str = Form(...)):
    print(username)

    async with async_session_maker() as session:
        result = await session.execute(
            select(AuthModel).where(AuthModel.username == username)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise HTTPException(
                status_code=409,
            )

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    str_hashed_password = hashed_password.decode("utf-8")

    new_user_data = AuthModel(username=username, hashed_psw=str_hashed_password)
    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_user_data)

    except IntegrityError:
        raise HTTPException(
            status_code=500,
        )
