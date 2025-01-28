from fastapi import APIRouter
from starlette.responses import HTMLResponse


homepage_router = APIRouter()


@homepage_router.get("/", response_class=HTMLResponse)
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
                align-items: flex-start;
                justify-content: center;
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }
            .center-container {
                margin-top: 10vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 1px;
            }
            .center-image {
                max-width: 300px;
                max-height: 300px;
                margin-bottom: 40px;
            }
            button {
                background-color: black;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="center-container">
            <img 
                src="https://github.com/user-attachments/assets/cd1f93f5-281e-4d28-b8a8-d4207b45a557" 
                alt="Find Friend Logo" 
                class="center-image"
            >
            <button onclick="window.location.href='http://127.0.0.1:8000/login'">Войти через Google</button>
        </div>
    </body>
    </html>
    """
