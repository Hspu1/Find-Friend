import bcrypt
from fastapi import APIRouter, Form
from sqlalchemy import select
from starlette.responses import RedirectResponse

from app.core import async_session_maker, AuthModel

login_router = APIRouter()


@login_router.post(path="/login")
async def login(username: str = Form(...), password: str = Form(...)):
    async with (async_session_maker() as session):
        result = await session.execute(
            select(AuthModel).where(AuthModel.username == username)
        )

        response = result.scalars().first()
        if (response is not None) and (
                bcrypt.checkpw(password.encode('utf-8'), response.hashed_psw.encode('utf-8'))
        ):
            return RedirectResponse(url="https://find-friend.onrender.com/showing_questionnaires", status_code=303)
