from fastapi import APIRouter, Form, HTTPException
from sqlalchemy.exc import IntegrityError
from starlette.responses import HTMLResponse
import bcrypt

from app.core import async_session_maker, AuthModel
from app.frontend.login_with_name import fake_new_names_db
from app.frontend.submit_name import fake_new_submit_names_db

password_entering_router = APIRouter()


@password_entering_router.get("/password_entering", response_class=HTMLResponse)
def html_landing():
    try:
        new_username = fake_new_names_db[-1]
    except IndexError:
        new_username = fake_new_submit_names_db[-1]

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
                    margin-top: 100px;
                    gap: 20px;
                }}
                .input-button-container {{
                    display: flex;
                    align-items: center;
                    gap: 10px;
                }}
                input {{
                    padding: 15px;
                    font-size: 18px;
                    width: 300px;
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
                <div class="input-button-container">
                    <input type="password" id="password" placeholder="Пароль" minlength="5" maxlength="12" required>
                    <button onclick="submitPassword()">Войти (на самом деле зарегестрироваться)</button>
                </div>
                <button onclick="window.location.href='http://127.0.0.1:8000/'">Придумать пароль</button>
                <button onclick="window.location.href='http://127.0.0.1:8000/login_with_name'">Назад</button>
            </div>

            <script>
                async function submitPassword() {{
                    const password = document.getElementById('password').value;
                    if (password.length >= 5 && password.length <= 12) {{
                        try {{
                            const response = await fetch('http://127.0.0.1:8000/submit_password', {{
                                method: 'POST',
                                headers: {{
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                }},
                                body: 'username={new_username}&password=' + encodeURIComponent(password)
                            }});
                            if (response.ok) {{
                                alert('Пароль сохранен');
                                window.location.href = 'http://127.0.0.1:8000/';
                            }} else {{
                                const errorText = await response.text();
                                console.error('Ошибка:', errorText);
                                alert('Ошибка при сохранении пароля');
                            }}
                        }} catch (error) {{
                            console.error('Ошибка сети:', error);
                            alert('Ошибка сети');
                        }}
                    }} else {{
                        alert('Пароль должен быть от 5 до 12 символов.');
                    }}
                }}
            </script>
        </body>
        </html>
    """


@password_entering_router.post("/submit_password")
async def submit_password(username: str = Form(...), password: str = Form(...)):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user_data = AuthModel(username=username, hashed_psw=str(hashed_password))

    print(
        f"username: {username}, "
        f"password: {password}, "
        f"hashed_password: {hashed_password}"
    )

    try:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_user_data)

                return {
                    "msg": "Success"
                }

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Пользователь уже существует"
        )
