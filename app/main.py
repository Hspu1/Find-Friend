import os

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastui import FastUI, AnyComponent, components as c, prebuilt_html
from fastui.events import GoToEvent
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from uvicorn import run

from app.google_auth import google_auth_router

app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Find Friend"
)
app.include_router(google_auth_router)


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


@app.get("/", response_class=HTMLResponse)
def html_landing():
    return prebuilt_html()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def root() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(
                    text="Google Auth", level=1
                ),
                c.Button(
                    text='Google',
                    on_click=GoToEvent(url="http://127.0.0.1:8000/login")
                )
            ],
        )
    ]


if __name__ == '__main__':
    run(
        app="main:app", reload=False, use_colors=True,
        host="127.0.0.1", port=8000
    )
