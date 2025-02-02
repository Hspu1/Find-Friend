import os

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from uvicorn import run

from app.frontend import (
    homepage_router, login_with_name_router, auth_denied_router,
    change_name_router, submit_name_router, password_entering_router,
    settings_router
)
from app.google_auth import google_auth_router


app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Find Friend"
)
app.include_router(homepage_router)
app.include_router(google_auth_router)
app.include_router(login_with_name_router)
app.include_router(auth_denied_router)
app.include_router(change_name_router)
app.include_router(submit_name_router)
app.include_router(password_entering_router)
app.include_router(settings_router)


app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY")
)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)


if __name__ == '__main__':
    run(
        app="main:app", reload=False, use_colors=True,
        host="127.0.0.1", port=8000
    )
