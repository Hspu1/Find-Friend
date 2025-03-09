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
                justify-content: center;
                width: auto;
                margin-top: 400px;
                gap: 60px;
            }
            .button-container button, .login-form button {
                background-color: rgba(15, 15, 15, 0.9);
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                font-size: 18px;
                font-weight: bold;
                border-radius: 4px;
                transition: background-color 0.2s ease;
            }
            .button-container button:hover, .login-form button:hover {
                background-color: rgba(40, 40, 40, 0.9);
            }
            .login-form {
                display: none;
                margin-top: 20px;
                text-align: left;
            }
            .login-form.show {
                display: block;
            }
            .login-form input {
                padding: 10px;
                margin-bottom: 10px;
                display: block;
                width: 100%;
                border: none;
                border-radius: 4px;
                background-color: rgba(30, 30, 30, 0.9);
                color: white;
            }
            .login-form button {
                width: 100%;
                text-align: left;
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
                max-width: 240px;
                max-height: 40px;
                flex-shrink: 0;
                padding: 10px 15px;
                box-sizing: border-box;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                font-size: 16px;
            }
            /* Стили для иконки "!" */
            .info-icon {
                position: fixed;
                top: 20px;
                left: 20px;
                width: 45px;
                height: 45px;
                background-color: rgba(15, 15, 15, 0.9);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 30px;
                font-weight: bold;
                color: white;
                cursor: pointer;
                transition: background-color 0.2s ease;
                box-shadow: 0 0 20px rgba(64, 224, 208, 0.7); /* Статическое свечение */
            }
            .info-icon:hover {
                background-color: rgba(40, 40, 40, 0.9);
            }
            /* Стили для плашки с текстом */
            .info-panel {
                position: fixed;
                top: 80px;
                left: 20px;
                background-color: rgba(15, 15, 15, 0.9);
                padding: 22.5px;
                border-radius: 7.5px;
                color: white;
                font-size: 21px;
                display: none;
                opacity: 0;
                transform: scale(0.9);
                animation: fade-in 0.5s ease-in-out forwards;
            }
            .info-panel.show {
                display: block;
            }
            @keyframes fade-in {
                0% {
                    opacity: 0;
                    transform: scale(0.9);
                }
                100% {
                    opacity: 1;
                    transform: scale(1);
                }
            }
            .info-panel p {
                margin: 0;
            }
            .info-panel .label {
                color: white;
                font-weight: bold;
                text-shadow:
                    0 0 10px white,
                    0 0 20px white,
                    0 0 30px rgba(255, 255, 255, 0.7); /* Яркое свечение */
            }
            .info-panel .value {
                color: #40E0D0;
                font-weight: bold;
                text-decoration: none;
                text-shadow:
                    0 0 10px #40E0D0,
                    0 0 20px #40E0D0,
                    0 0 30px rgba(64, 224, 208, 0.7); /* Свечение текста */
            }
        </style>
    </head>
    <body>
        <div class="error-message" id="error-message">
            <span id="error-text"></span>
            <span class="close-error" onclick="closeError()">×</span>
        </div>
        <div class="info-icon" onclick="toggleInfoPanel()">!</div>
        <div class="info-panel" id="info-panel">
            <p><span class="label">Телеграм:</span> <a href="https://t.me/Hspu1" class="value">@Hspu1</a></p>
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
                <button class="register-button" onclick="window.location.href='https://find-friend.onrender.com/login'">Зарегистрироваться</button>
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
            function toggleInfoPanel() {
                const infoPanel = document.getElementById('info-panel');
                infoPanel.classList.toggle('show');
            }
        </script>
    </body>
    </html>
    """
