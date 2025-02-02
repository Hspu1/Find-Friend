from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.google_auth import fake_firstnames_db


login_with_name_router = APIRouter()
fake_new_names_db = []


@login_with_name_router.get("/login_with_name", response_class=HTMLResponse)
def html_landing():
    fake_new_names_db.append(fake_firstnames_db[-1])

    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
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
                }}
                .button-container {{
                    display: flex;
                    flex-direction: column;
                    gap: 20px;
                    align-items: center;
                    margin-top: 100px;
                }}
                button {{
                    background-color: black;
                    color: white;
                    border: none;
                    padding: 20px 40px;
                    cursor: pointer;
                    font-size: 18px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="button-container">
                <button onclick="window.location.href='http://127.0.0.1:8000/password_entering'">
                    Войти как {fake_firstnames_db[-1]}
                </button>
                <button onclick="window.location.href='http://127.0.0.1:8000/change_name'">
                    Изменить имя
                </button>
                <button onclick="window.location.href='http://127.0.0.1:8000/'">
                    Назад
                </button>
            </div>
        </body>
        </html>
    """
