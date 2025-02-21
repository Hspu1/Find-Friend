from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.exc import IntegrityError

from app.core import async_session_maker, UsersModel

save_questionnaire_user_data_router = APIRouter()


@save_questionnaire_user_data_router.post(path="/save_questionnaire_user_data", status_code=201)
async def save_data(request: Request):
    form_data = await request.json()

    # int(form_data["age"]) - ВАЖНО: На стороне фронтенда
    # поле для ввода возраста имеет тип ТЕКСТА, а НЕ ЧИСЛА
    questionnaire_user_data = UsersModel(
        username=form_data["username"], age=int(form_data["age"]),
        hobbies=form_data["hobbies"], bio=form_data["bio"],
        telegram=form_data["telegram"], email=form_data["email"],
        phone=form_data["phone"], other=form_data["otherContactInfo"]
    )

    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(questionnaire_user_data)

    except IntegrityError:
        raise HTTPException(status_code=409)
