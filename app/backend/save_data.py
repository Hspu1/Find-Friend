from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker

save_data_router = APIRouter()


@save_data_router.post(path="/save_data", status_code=201)
async def save_data(request: Request):
    form_data = await request.json()
    print(
        "Файл с кодом - save_data.py",
        {
            "Имя": form_data["username"],
            "Возраст": form_data["age"],
            "Хобби": form_data["hobbies"],
            "О себе": form_data["bio"],
            "Телеграмм": form_data["telegram"],
            "Email": form_data["email"],
            "Телефон": form_data["phone"],
            "Другое": form_data["otherContactInfo"]
        }
    )

    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_user_data)


    except IntegrityError:
        raise HTTPException(status_code=409)
