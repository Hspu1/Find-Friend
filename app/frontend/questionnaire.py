from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.backend.get_last_username import get_latest_username

questionnaire_router = APIRouter()


@questionnaire_router.get("/questionnaire", response_class=HTMLResponse)
async def html_landing():
    username = await get_latest_username()

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
                align-items: center;
                justify-content: flex-start;
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }}
            .container {{
                text-align: center;
                width: 100%;
                margin-top: 100px;
            }}
            h1 {{
                color: white;
                font-weight: bold;
                text-shadow: 2px 2px 0 black, -1px -1px 0 black, 
                             1px -1px 0 black, -1px 1px 0 black, 
                             1px 1px 0 black;
            }}
            .button-group {{
                margin-top: 270px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .card {{
                padding: 10px 40px;
                font-size: 18px;
                font-weight: bold;
                background-color: rgba(15, 15, 15, 0.9); /* Темнее, чем поля для ввода */
                color: white;
                border: none;
                cursor: pointer;
                margin-top: 5px;
                border-radius: 4px; /* Чуточку закругленные углы */
                transition: background-color 0.2s ease;
            }}
            .card:hover {{
                background-color: rgba(40, 40, 40, 0.9); /* Светлее при наведении */
            }}
            .input-field {{
                display: none;
                margin-top: 10px;
                width: 300px;
                padding: 10px;
                font-size: 16px;
                border: none;
                border-radius: 4px; /* Чуточку закругленные углы */
                background-color: rgba(30, 30, 30, 0.9); /* Поля для ввода светлее кнопок */
                color: white;
                transition: opacity 0.3s ease, transform 0.3s ease;
                opacity: 0;
                transform: translateY(-10px);
            }}
            .input-field.show {{
                opacity: 1;
                transform: translateY(0);
            }}
            textarea {{
                resize: none;
            }}
            #contact-me-container {{
                display: none;
                margin-top: 10px;
                transition: opacity 0.3s ease, transform 0.3s ease;
                opacity: 0;
                transform: translateY(-10px);
            }}
            #contact-me-container.show {{
                opacity: 1;
                transform: translateY(0);
            }}
            #contact-me-container input {{
                width: 300px;
                padding: 10px;
                font-size: 16px;
                border: none;
                border-radius: 4px; /* Чуточку закругленные углы */
                background-color: rgba(30, 30, 30, 0.9); /* Поля для ввода светлее кнопок */
                color: white;
                margin-bottom: 10px;
                transition: opacity 0.3s ease, transform 0.3s ease;
            }}
            #done-button {{
                margin-top: 20px;
                padding: 15px 30px;
                font-size: 20px;
                background-color: rgba(15, 15, 15, 0.9); /* Темнее, чем поля для ввода */
                color: white;
                border: none;
                border-radius: 4px; /* Чуточку закругленные углы */
                cursor: pointer;
                transition: background-color 0.2s ease;
            }}
            #done-button:hover {{
                background-color: rgba(40, 40, 40, 0.9); /* Светлее при наведении */
            }}
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Имя - {username}</h1> <!-- Имя пользователя -->

            <div class="button-group">
                <button class='card' onclick='showInput("age")'>Возраст</button>
                <input type="text" id="age-input" class="input-field" maxlength="3" oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 3);">
                <button class='card' onclick='showInput("hobbies")'>Хобби</button>
                <textarea id='hobbies-input' class='input-field' rows='2' cols='30' maxlength='50'></textarea>

                <button class='card' onclick='showInput("bio")'>О себе</button>
                <textarea id='bio-textarea' class='input-field' rows='5' cols='30' maxlength='100'></textarea>

                <button class='card' onclick='showContactMe()'>Связаться со мной</button>

                <div id='contact-me-container'>
                    <input type='text' id='telegram-input' placeholder='Телеграмм' maxlength='50'><br/>
                    <input type='email' id='email-input' placeholder='Email' maxlength='50'><br/>
                    <input type='tel' id='phone-input' placeholder='Телефон' maxlength='30'><br/>
                    <input type='text' id='other-contact-info-input' placeholder='Другое' maxlength='100'><br/>
                </div>

                <button class='card' id='done-button' onclick='submitForm()'>Готово!</button>
            </div>
        </div>

        <script>
            function showInput(inputId) {{
                const input = document.getElementById(inputId + "-input") || document.getElementById(inputId + "-textarea");

                if (input) {{
                    if (input.classList.contains('show')) {{
                        input.classList.remove('show');
                        setTimeout(() => input.style.display = 'none', 300); // Задержка для анимации
                    }} else {{
                        const allInputs = document.querySelectorAll('.input-field');
                        allInputs.forEach(field => {{
                            if (field !== input) {{
                                field.classList.remove('show');
                                setTimeout(() => field.style.display = 'none', 300); // Задержка для анимации
                            }}
                        }});

                        input.style.display = 'block';
                        setTimeout(() => input.classList.add('show'), 10); // Задержка для анимации
                        input.focus();
                    }}
                }}
            }}

            function showContactMe() {{
                const contactContainer = document.getElementById("contact-me-container");

                if (contactContainer.classList.contains('show')) {{
                    contactContainer.classList.remove('show');
                    setTimeout(() => contactContainer.style.display = 'none', 300); // Задержка для анимации
                }} else {{
                    contactContainer.style.display = 'block';
                    setTimeout(() => contactContainer.classList.add('show'), 10); // Задержка для анимации
                }}
            }}

            function submitForm() {{
                const ageInput = document.getElementById("age-input");

                if (!ageInput.value) {{
                    alert("Вы не заполнили обязательное поле для ввода возраста");
                    return;
                }}

                const data = {{
                    username: "{username}",
                    age: ageInput.value,
                    hobbies: document.getElementById("hobbies-input").value || null,
                    bio: document.getElementById("bio-textarea").value || null,
                    telegram: document.getElementById("telegram-input").value || null,
                    email: document.getElementById("email-input").value || null,
                    phone: document.getElementById("phone-input").value || null,
                    otherContactInfo: document.getElementById("other-contact-info-input").value || null
                }};

                fetch("http://127.0.0.1:8000/save_questionnaire_user_data", {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify(data)
                }})
                .then(response => {{
                    if (response.ok) {{
                        window.location.href = "http://127.0.0.1:8000/showing_questionnaires";
                    }} else {{
                        return response.text().then(text => {{ throw new Error(text); }});
                    }}
                }})
                .catch(error => {{
                    console.error("Ошибка:", error);
                    alert("Ошибка при отправке данных: " + error.message);
                }});
            }}
        </script>
    </body>
    </html>
    """

    return html_content
