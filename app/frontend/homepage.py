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
                gap: 40px; 
            }
            .glow-text {
                font-size: 48px; 
                font-weight: bold; 
                color: #32CD32; 
                text-shadow:
                    0 0 10px #32CD32,
                    0 0 20px #32CD32,
                    0 0 30px rgba(50, 205, 50, 0.5);
                letter-spacing: -1px;
            }
            .glow-text span {
                display: inline-block;
                animation: color-animation 0.5s infinite alternate, scale-animation 1s infinite alternate; 
            }
            @keyframes color-animation {
                from {
                    color: #32CD32; 
                    text-shadow:
                        0 0 10px #32CD32,
                        0 0 20px #32CD32,
                        0 0 30px rgba(50, 205, 50, 0.5);
                }
                to {
                    color: #40E0D0; 
                    text-shadow:
                        0 0 10px #40E0D0,
                        0 0 20px #40E0D0,
                        0 0 30px rgba(64,224,208,0.5);
                }
            }
            @keyframes scale-animation {
                from {
                    transform: translateY(0) scale(1);
                }
                to {
                    transform: translateY(-10px) scale(1.2);
                }
            }
            button {
                background-color: black;
                color: white;
                border: none;
                padding: 20px 40px;
                cursor: pointer;
                font-size: 18px;
                font-weight: bold;
                margin-top: 250px; 
            }
        </style>
    </head>
    <body>
        <div class="center-container">
            <div class="glow-text">
              <span style="animation-delay: 0s;">F</span>
              <span style="animation-delay: 0.05s;">i</span>
              <span style="animation-delay: 0.1s;">n</span>
              <span style="animation-delay: 0.15s;">d</span>
              <span style="animation-delay: 0.2s;"> </span>
              <span style="animation-delay: 0.25s;">F</span>
              <span style="animation-delay: 0.3s;">r</span>
              <span style="animation-delay: 0.35s;">i</span>
              <span style="animation-delay: 0.4s;">e</span>
              <span style="animation-delay: 0.45s;">n</span>
              <span style="animation-delay: 0.5s;">d</span>
            </div>
            <button onclick="window.location.href='http://127.0.0.1:8000/login'">Войти через Google</button>
        </div>
    </body>
    </html>
    """
