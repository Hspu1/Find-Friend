from fastapi import APIRouter, Request

save_data_router = APIRouter()


@save_data_router.post(path="/save_data", status_code=201)
async def save_data(request: Request):
    form_data = await request.json()

    print({
        "Имя": form_data["username"],
        "Возраст": form_data["age"],
        "Хобби": form_data["hobbies"],
        "О себе": form_data["bio"],
        "Телеграмм": form_data["telegram"],
        "Email": form_data["email"],
        "Телефон": form_data["phone"],
        "Другое": form_data["otherContactInfo"]
    })

    return {"message": f"{form_data['username']}'s data saved successfully"}
