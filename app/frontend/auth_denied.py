from fastapi import APIRouter
from starlette.responses import HTMLResponse

auth_denied_router = APIRouter()


@auth_denied_router.get("/auth_denied", response_class=HTMLResponse)
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
                .content-container {{
                    display: flex;
                    flex-direction: column;
                    gap: 20px;
                    align-items: center;
                    margin-top: 100px;
                }}
                .message {{
                    color: white;
                    font-size: 24px;
                    text-align: center;
                }}
                button {{
                    background-color: black;
                    color: white;
                    border: none;
                    padding: 20px 40px;
                    cursor: pointer;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <div class="content-container">
                <div class="message">
                    Авторизация была отклонена
                </div>
                <button onclick="window.location.href='http://127.0.0.1:8000/'">
                    Назад
                </button>
            </div>
        </body>
        </html>
        """
