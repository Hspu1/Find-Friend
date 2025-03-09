from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.frontend.login_with_name import fake_new_names_db
from app.frontend.submit_name import fake_new_submit_names_db

password_entering_router = APIRouter()


@password_entering_router.get("/password_entering", response_class=HTMLResponse)
def html_landing():
    try:
        new_username = fake_new_names_db[-1]
    except IndexError:
        new_username = fake_new_submit_names_db[-1]

    html_content = f"""
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
                    gap: 20px;
                    position: absolute; /* Абсолютное позиционирование */
                    top: 50%; /* Позиция сверху */
                    left: 50%; /* Позиция слева */
                    transform: translate(-50%, -45px); /* Смещение вверх на 45 пикселей */
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
                    border: none;
                    border-radius: 4px;
                    background-color: rgba(30, 30, 30, 0.9);
                    color: white;
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
                <div class="input-button-container">
                    <input type="password" id="password" placeholder="Пароль" minlength="5" maxlength="12" required>
                    <button onclick="submitPassword()">Зарегестрироваться</button>
                </div>
                <button onclick="window.location.href='https://find-friend.onrender.com/login_with_name'">Назад</button>
            </div>

            <script>
                async function submitPassword() {{
                    const password = document.getElementById('password').value;
                    if (password.length >= 5 && password.length <= 12) {{
                        try {{
                            const response = await fetch('https://find-friend.onrender.com/submit_password', {{
                                method: 'POST',
                                headers: {{
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                }},
                                body: 'username=' + encodeURIComponent('{new_username}') + '&password=' + encodeURIComponent(password)
                            }});
                            if (response.ok) {{
                                alert('Данные успешно сохранены');
                                window.location.href = 'https://find-friend.onrender.com/questionnaire';
                            }} else {{
                                const errorText = await response.text();
                                console.error('Ошибка:', errorText);
                                alert('Пользователь с таким именем уже существует');
                                window.location.href = 'https://find-friend.onrender.com/change_name';
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

    return html_content
