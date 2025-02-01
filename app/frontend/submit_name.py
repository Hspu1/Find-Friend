from fastapi import Form, APIRouter
from starlette.responses import HTMLResponse

submit_name_router = APIRouter()


@submit_name_router.post("/submit_name", response_class=HTMLResponse)
def submit_name(new_name: str = Form()):
    print(new_name)
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
                }}
                .container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 20px;
                    margin-top: 100px;
                }}
                h1 {{
                    color: white;
                    font-weight: bold;
                    text-shadow: 2px 2px 0 black, -1px -1px 0 black, 
                                 1px -1px 0 black, -1px 1px 0 black, 
                                 1px 1px 0 black;
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
            <div class="container">
                <h1>Имя изменено на {new_name}</h1>
                <button onclick="window.location.href='http://127.0.0.1:8000/password_entering'">Войти под новым именем</button>
                <button onclick="window.location.href='http://127.0.0.1:8000/change_name'">Назад</button>
            </div>
        </body>
        </html>
    """
