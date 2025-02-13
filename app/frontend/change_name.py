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
                    margin-top: 100px;
                }
                input {
                    padding: 15px;
                    font-size: 18px;
                    width: 300px;
                }
                button {
                    background-color: black;
                    color: white;
                    border: none;
                    padding: 20px 40px;
                    cursor: pointer;
                    font-size: 18px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <form action="/submit_name" method="post">
                    <input type="text" name="new_name" placeholder="Введите новое имя" maxlength="20" required>
                    <button type="submit">Изменить имя</button>
                </form>
                <button onclick="window.location.href='http://127.0.0.1:8000/login_with_name'">Назад</button>
            </div>
        </body>
        </html>
    """
