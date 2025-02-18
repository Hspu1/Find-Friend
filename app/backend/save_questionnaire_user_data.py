from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, UsersModel, ContactsModel

save_questionnaire_user_data_router = APIRouter()


@save_questionnaire_user_data_router.post(path="/save_questionnaire_user_data", status_code=201)
async def save_data(request: Request):
    form_data = await request.json()
    print(
        "Файл с кодом - save_questionnaire_user_data.py",
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

    # int(form_data["age"]) - ВАЖНО: На стороне фронтенда
    # поле для ввода возраста имеет тип ТЕКСТА, а НЕ ЧИСЛА
    questionnaire_user_data = UsersModel(
        username=form_data["username"], age=int(form_data["age"]),
        hobbies=form_data["hobbies"], bio=form_data["bio"],
        # contact_me=form_data["username"]
    )

    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(questionnaire_user_data, ContactsModel(username="TESTING_FEATURE"))

    except IntegrityError:
        raise HTTPException(status_code=409)
