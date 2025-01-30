from fastapi import APIRouter
from starlette.responses import HTMLResponse


change_name_router = APIRouter()


@change_name_router.get("/change_name", response_class=HTMLResponse)
def html_landing():
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
                .container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}
                .input-container {{
                    display: flex;
                    flex-direction: row;
                    gap: 20px;
                    margin-top: 50px;
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
                .back-button {{
                    margin-top: 30px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="input-container">
                    <input type="text" id="new-name" placeholder="Введите новое имя" maxlength="20" required>
                    <button onclick="submitName()">Изменить имя</button>
                </div>                    
                <button class="back-button" onclick="window.location.href='/login_with_name'">Назад</button>
            </div>

            <script>
                function submitName() {{
                    const newName = document.getElementById('new-name').value;

                    if (newName.length > 0 && newName.length <= 20) {{
                        window.location.href = `/login_with_name?name=${{newName}}`;
                    }} else {{
                        alert('Имя должно быть от 1 до 20 символов.');
                    }}
                }}
            </script>
        </body>
        </html>
    """
