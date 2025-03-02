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
                    flex-direction: column;
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
                    position: absolute; /* Абсолютное позиционирование */
                    top: 50%; /* Позиция сверху */
                    left: 50%; /* Позиция слева */
                    transform: translate(-50%, -60px); /* Смещение вверх на 60 пикселей */
                }}
                button {{
                    background-color: rgba(15, 15, 15, 0.9);
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    cursor: pointer;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 4px;
                    transition: background-color 0.2s ease;
                }}
                button:hover {{
                    background-color: rgba(40, 40, 40, 0.9);
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
