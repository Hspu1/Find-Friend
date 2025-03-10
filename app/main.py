import os

from alembic import command, config
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from uvicorn import run

from app.backend import (
    submit_password_router, save_questionnaire_user_data_router,
    get_latest_username_router, login_router, get_all_users_data_router
)
from app.frontend import (
    homepage_router, login_with_name_router, auth_denied_router,
    change_name_router, submit_name_router, password_entering_router,
    questionnaire_router, showing_questionnaires
)
from app.google_auth import google_auth_router


app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Find Friend"
)


app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY")
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

# Backend
app.include_router(submit_password_router)
app.include_router(save_questionnaire_user_data_router)
app.include_router(get_latest_username_router)
app.include_router(login_router)
app.include_router(get_all_users_data_router)

# Frontend
app.include_router(homepage_router)
app.include_router(google_auth_router)
app.include_router(login_with_name_router)
app.include_router(auth_denied_router)
app.include_router(change_name_router)
app.include_router(submit_name_router)
app.include_router(password_entering_router)
app.include_router(questionnaire_router)
app.include_router(showing_questionnaires)


if __name__ == "__main__":
    alembic_cfg = config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv("DB_URL"))

    command.upgrade(alembic_cfg, "head")
    run(
        app="app.main:app", host="0.0.0.0",
        port=80, reload=True, use_colors=True
    )
