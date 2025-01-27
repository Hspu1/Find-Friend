import os

from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastui import FastUI, AnyComponent, components as c
from fastui.components import Link
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run


load_dotenv()

app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Find Friend"
)


origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)


oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    },
)


@app.get(path="/login", tags=["auth"], status_code=200)
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


# class User(BaseModel):
#     id: int
#     name: str
#     dob: date = Field(title='Date of Birth')
#
#
# users = [
#     User(id=1, name='John', dob=date(1990, 1, 1)),
#     User(id=2, name='Jack', dob=date(1991, 1, 1)),
#     User(id=3, name='Jill', dob=date(1992, 1, 1)),
#     User(id=4, name='Jane', dob=date(1993, 1, 1)),
# ]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    # return [
    #     c.Page(
    #         components=[
    #             c.Heading(text='Users', level=2),
    #             c.Table(
    #                 data=users,
    #                 columns=[
    #                     DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
    #                     DisplayLookup(field='dob', mode=DisplayMode.date),
    #                 ],
    #             ),
    #         ]
    #     ),
    # ]
    return [
        c.Page(
            components=[
                c.Button(
                    text='Google',
                    on_click=Link(url='/google_auth_login')
                )
            ],
            title='Google Auth'
        )
    ]


# @app.get("/api/user/{user_id}/", response_model=FastUI, response_model_exclude_none=True)
# def user_profile(user_id: int) -> list[AnyComponent]:
#     try:
#         user = next(u for u in users if u.id == user_id)
#     except StopIteration:
#         raise HTTPException(status_code=404, detail="User not found")
#     return [
#         c.Page(
#             components=[
#                 c.Heading(text=user.name, level=2),
#                 c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
#                 c.Details(data=user),
#             ]
#         ),
#     ]
#
#
# @app.get('/{path:path}')
# async def html_landing() -> HTMLResponse:
#     return HTMLResponse(prebuilt_html(title='FastUI Demo'))


if __name__ == '__main__':
    run(
        app="main:app", reload=False, use_colors=True,
        host="127.0.0.1", port=8000
    )
