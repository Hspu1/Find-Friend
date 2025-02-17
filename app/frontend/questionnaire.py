from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.backend.get_last_username import get_latest_username

questionnaire_router = APIRouter()


@questionnaire_router.get("/questionnaire", response_class=HTMLResponse)
async def html_landing():
    username = await get_latest_username()  # Получаем имя пользователя
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
                        justify-content: flex-start; /* Выравнивание сверху */
                        background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                        background-size: cover;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-attachment: fixed;
                    }}
                    .container {{
                       text-align: center;
                       width: 100%;
                       margin-top: 100px; /* Смещение текста вниз на 100 пикселей */
                    }}
                    h1 {{
                        color: white;
                        font-weight: bold;
                        text-shadow: 2px 2px 0 black, -1px -1px 0 black, 
                                     1px -1px 0 black, -1px 1px 0 black, 
                                     1px 1px 0 black;
                    }}
                    .button-group {{
                       margin-top: 270px; /* Смещаем группу кнопок ниже на дополнительные 20 пикселей */
                       display: flex;
                       flex-direction: column; /* Располагаем кнопки вертикально */
                       align-items: center; /* Центрируем кнопки */
                    }}
                    .card {{
                       padding: 10px 40px;
                       font-size: 18px;
                       font-weight: bold;
                       background-color: black;
                       color: white;
                       border: none;
                       cursor: pointer;
                       margin-top: 5px; /* Уменьшенный отступ между кнопками */
                    }}
                    .input-field {{
                        display: none; /* Поля скрыты по умолчанию */
                        margin-top: 10px; /* Отступ сверху для полей ввода */
                    }}
                    input, textarea {{
                        width: 300px;
                        height: 30px;
                        font-size: 16px;
                        margin-bottom: 10px; /* Уменьшенный отступ между полями */
                        border: none;
                        border-bottom: solid black 2px;
                    }}
                    textarea {{
                        resize: none;
                    }}
                    #contact-me-container {{
                      display:none ;
                      margin-top: 10px; /* Уменьшенный отступ сверху для контейнера */
                   }}
                   #done-button {{
                       margin-top: 20px; /* Отступ сверху для кнопки "Готово" */
                       padding: 15px 30px; /* Увеличение размера кнопки */
                       font-size: 20px; /* Увеличение шрифта для кнопки "Готово" */
                   }}
                </style>
            </head>
            <body>
                <div class='container'>
                    <h1>Имя - {username}</h1> <!-- Имя пользователя -->

                    <div class="button-group">
                        <button class='card' onclick='showInput("age")'>Возраст</button>
                        <input type='text' id='age-input' class='input-field' minlength="1" maxlength="3" required>

                        <button class='card' onclick='showInput("hobbies")'>Хобби</button>
                        <input type='text' id='hobbies-input' class='input-field'>

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

                        // Переключаем отображение поля
                        if (input) {{
                            // Если поле уже открыто, скрываем его
                            if (input.style.display === 'block') {{
                                input.style.display = 'none';
                            }} else {{
                                // Скрываем все другие поля ввода перед показом нового
                                const allInputs = document.querySelectorAll('.input-field');
                                allInputs.forEach(field => field.style.display = 'none');

                                // Показываем текущее поле
                                input.style.display = 'block';
                                input.focus(); // Фокус на поле ввода после его отображения
                            }}
                        }}
                    }}

                    function showContactMe() {{
                        const contactContainer = document.getElementById("contact-me-container");

                        // Переключаем отображение контейнера
                        contactContainer.style.display = (contactContainer.style.display === "none") ? "block" : "none";
                    }}

                    function submitForm() {{
                        const ageInput = document.getElementById("age-input");

                        // Проверяем, заполнено ли поле возраста
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

                        fetch("http://127.0.0.1:8000/save_data", {{
                            method: "POST",
                            headers: {{ "Content-Type": "application/json" }},
                            body: JSON.stringify(data)
                        }})
                        .then(response => {{
                            if (response.ok) {{
                                window.location.href = "http://127.0.0.1:8000";
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
