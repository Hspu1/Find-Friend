import bcrypt
from fastapi import Form, APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, AuthModel


submit_password_router = APIRouter()


@submit_password_router.post(path="/submit_password", status_code=201)
async def submit_password(username: str = Form(...), password: str = Form(...)):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user_data = AuthModel(username=username, hashed_psw=str(hashed_password))

    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_user_data)

    except IntegrityError:
        raise HTTPException(status_code=409)
