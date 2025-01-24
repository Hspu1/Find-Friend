# from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse, HTMLResponse
# from uvicorn import run
# from fastui import FastUI, components as c
#
#
# app = FastAPI(
#     default_response_class=ORJSONResponse,
#     title="Find Friend"
# )
#
#
# if __name__ == '__main__':
#     run(
#         app="main:app", reload=False, use_colors=True,
#         host="127.0.0.1", port=8000
#     )
from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from pydantic import BaseModel, Field
from uvicorn import run

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    dob: date = Field(title='Date of Birth')


users = [
    User(id=1, name='John', dob=date(1990, 1, 1)),
    User(id=2, name='Jack', dob=date(1991, 1, 1)),
    User(id=3, name='Jill', dob=date(1992, 1, 1)),
    User(id=4, name='Jane', dob=date(1993, 1, 1)),
]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(text='Users', level=2),
                c.Table(
                    data=users,
                    columns=[
                        DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
                        DisplayLookup(field='dob', mode=DisplayMode.date),
                    ],
                ),
            ]
        ),
    ]


@app.get("/api/user/{user_id}/", response_model=FastUI, response_model_exclude_none=True)
def user_profile(user_id: int) -> list[AnyComponent]:
    try:
        user = next(u for u in users if u.id == user_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="User not found")
    return [
        c.Page(
            components=[
                c.Heading(text=user.name, level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=user),
            ]
        ),
    ]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))


if __name__ == '__main__':
    run(
        app="main:app", reload=False, use_colors=True,
        host="127.0.0.1", port=8000
    )
