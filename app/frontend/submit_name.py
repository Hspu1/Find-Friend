from fastapi import Form, APIRouter
from starlette.responses import HTMLResponse

from app.frontend.login_with_name import fake_new_names_db

submit_name_router = APIRouter()
fake_new_submit_names_db = []


@submit_name_router.post("/submit_name", response_class=HTMLResponse, status_code=201)
def submit_name(new_name: str = Form()):
    fake_new_submit_names_db.append(new_name)
    fake_new_names_db.append(new_name)

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
                .container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 15px; /* Уменьшил расстояние между объектами */
                    position: absolute; /* Абсолютное позиционирование */
                    top: 50%; /* Позиция сверху */
                    left: 50%; /* Позиция слева */
                    transform: translate(-50%, -80px); /* Смещение вниз на 20 пикселей (117px - 20px = 97px) */
                }}
                .back-button {{
                    margin-top: 37px; /* Смещение кнопки "Назад" вниз на 15 пикселей дополнительно */
                }}
                h1 {{
                    color: white;
                    font-weight: bold;
                    text-shadow: 2px 2px 0 black, -1px -1px 0 black, 
                                 1px -1px 0 black, -1px 1px 0 black, 
                                 1px 1px 0 black;
                    font-size: 28px;
                }}
                .glow {{
                    text-shadow: 0 0 10px white, 0 0 20px white, 0 0 30px white;
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
            <div class="container">
                <h1>Имя изменено на <span class="glow">{new_name}</span></h1>
                <button onclick="window.location.href='https://find-friend.onrender.com/password_entering'">Войти под новым именем</button>
                <div class="back-button">
                    <button onclick="window.location.href='https://find-friend.onrender.com/change_name'">Назад</button>
                </div>
            </div>
        </body>
        </html>
    """
