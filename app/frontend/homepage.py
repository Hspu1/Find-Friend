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
            .button-container {
                display: flex;
                justify-content: center; /* Измените на center или space-between */
                width: auto; /* Автоматическая ширина */
                margin-top: 400px;
                gap: 20px;
            }
            .button-container button {
                background-color: black;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
            }
            .login-form {
                display: none;
                margin-top: 20px;
            }
            .login-form.show {
                display: block;
            }
            .login-form input {
                padding: 10px;
                margin-bottom: 10px;
                display: block;
                width: 100%;
            }
            .login-form button {
                background-color: black;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                font-weight: bold;
                width: 100%;
            }
            .error-message {
                position: fixed;
                top: 30px; 
                left: 40px; 
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
                display: none;
            }
            .error-message.show {
                display: block;
            }
            .close-error {
                float: right;
                margin-left: 10px; 
                cursor: pointer;
            }
            .login-form-container {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .register-button {
                max-width: 200px; /* Максимальная ширина */
                max-height: 40px; /* Максимальная высота */
                flex-shrink: 0; /* Чтобы кнопка не сжималась */
            }
        </style>
    </head>
    <body>
        <div class="error-message" id="error-message">
            <span id="error-text"></span>
            <span class="close-error" onclick="closeError()">×</span>
        </div>
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
            <div class="button-container">
                <div class="login-form-container">
                    <button id="login-btn" onclick="showLoginForm()">Войти в аккаунт</button>
                    <div class="login-form" id="login-form">
                        <form action="/login" method="post">
                            <input type="text" id="username" name="username" maxlength="20" placeholder="Имя" required 
                                   oninvalid="this.setCustomValidity('Пожалуйста, введите ваше имя')" 
                                   oninput="this.setCustomValidity('')">
                            <input type="password" id="password" name="password" minlength="5" maxlength="12" placeholder="Пароль" required 
                                   oninvalid="this.setCustomValidity('Введённый пароль содержит меньше 5 символов')" 
                                   oninput="this.setCustomValidity('')">
                            <button type="submit"><b>Готово!</b></button>
                        </form>
                    </div>
                </div>
                <button class="register-button" onclick="window.location.href='http://127.0.0.1:8000/login'">Зарегистрироваться</button>
            </div>
        </div>
        <script>
            function showLoginForm() {
                const loginForm = document.getElementById('login-form');
                const errorMessage = document.getElementById('error-message');

                if (loginForm.classList.contains('show')) {
                    loginForm.classList.remove('show');
                    errorMessage.classList.remove('show');
                } else {
                    loginForm.classList.add('show');
                }
            }
            function closeError() {
                const errorMessage = document.getElementById('error-message');
                errorMessage.classList.remove('show');
            }
        </script>
    </body>
    </html>
    """
