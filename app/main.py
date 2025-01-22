from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from uvicorn import run


app = FastAPI(
    default_response_class=ORJSONResponse,
    title="Find Friend"
)


if __name__ == '__main__':
    run(
        app="app/main:app", reload=False, use_colors=True,
        host="127.0.0.1", port=8000
    )
