from fastapi import APIRouter
from starlette.responses import HTMLResponse

change_name_router = APIRouter()


@change_name_router.get("/change_name", response_class=HTMLResponse)
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
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                    background-attachment: fixed;
                }
                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 20px;
                    position: absolute; /* Абсолютное позиционирование */
                    top: 50%; /* Позиция сверху */
                    left: 50%; /* Позиция слева */
                    transform: translate(-50%, -45px); /* Смещение вверх на 45 пикселей */
                }
                input {
                    padding: 15px;
                    font-size: 18px;
                    width: 300px;
                    border: none;
                    border-radius: 4px;
                    background-color: rgba(30, 30, 30, 0.9);
                    color: white;
                }
                button {
                    background-color: rgba(15, 15, 15, 0.9);
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    cursor: pointer;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 4px;
                    transition: background-color 0.2s ease;
                }
                button:hover {
                    background-color: rgba(40, 40, 40, 0.9);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <form action="/submit_name" method="post">
                    <input type="text" name="new_name" placeholder="Введите новое имя" maxlength="20" required>
                    <button type="submit">Изменить имя</button>
                </form>
                <button onclick="window.location.href='https://find-friend.onrender.com/login_with_name'">Назад</button>
            </div>
        </body>
        </html>
    """
