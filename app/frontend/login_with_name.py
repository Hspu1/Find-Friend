from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.google_auth import fake_firstnames_db


login_with_name_router = APIRouter()


@login_with_name_router.get("/login_with_name", response_class=HTMLResponse)
def html_landing():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }
            button {
                background-color: black;
                color: white;
                border: none;
                padding: 20px 40px;
                cursor: pointer;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <button onclick="window.location.href='http://127.0.0.1:8000/'">
            Войти как {}
        </button>
    </body>
    </html>
    """
