from fastapi import APIRouter
from starlette.responses import HTMLResponse


questionnaire_router = APIRouter()


@questionnaire_router.get("/questionnaire", response_class=HTMLResponse)
def html_landing():
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
                        align-items: center;
                        justify-content: center;
                        background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                        background-size: cover;
                        background-repeat: no-repeat;
                        background-position: center;
                        background-attachment: fixed;
                    }}

                    .container {{
                       text-align:center;
                    }}

                    .card {{
                       padding-top :10px;
                       padding-bottom :10px;
                       padding-left :40px;
                       padding-right :40px;

                        font-size :18px ;
                        font-weight :bold ;
                        background-color:black ;
                        color:white ;
                        border:none ;
                        cursor: pointer;
					}}

					input[type="number"], input[type="text"], textarea, input[type="email"], input[type="tel"]{{
						width :300px ;
						height :30px ;
						font-size :16px ;
						margin-bottom :20px ;
						border:none ;
    					border-bottom:solid black 2px;

					}}

    				textarea{{
    					    resize:none ;
    						border:none ;
    						border-bottom:solid black 2px;

    				}}

                    #contact-me-container {{
                      display:none ;

                   }}

                   /* Added margin to separate "Contact Me" and "Done" buttons */
                   #done-button {{
                       margin-top: 20px;
                   }}

                </style>

            </head>

            <body>
                <div class='container'>
                    <div id='username'>Имя - example_name_blyat</div><br/>

                    <button class='card' onclick='showInput("age")'>Возраст</button><br/>
                    <input type='number' id='age-input' min='1' max='150' placeholder='Введите возраст' style='display:none;' required><br/>

                    <button class='card' onclick='showInput("hobbies")'>Хобби</button><br/>
                    <input type='text' id='hobbies-input' placeholder='Введите хобби' style='display:none;'><br/>

                    <button class='card' onclick='showInput("bio")'>О себе</button><br/>
                    <textarea id='bio-textarea' rows='5' cols='30' maxlength='100' placeholder='О себе' style='display:none;'></textarea><br/>

                    <button class='card' onclick='showContactMe()'>Связаться со мной</button><br/>

                    <div id='contact-me-container' style='display:none;'>
                        <input type='text' id='telegram-input' placeholder='Телеграмм' maxlength='50'><br/>
                        <hr/>

                        <input type='email' id='email-input' placeholder='Email' maxlength='50'><br/>
                        <hr/>

                        <input type='tel' id='phone-input' placeholder='Телефон' maxlength='30'><br/>
                        <hr/>

                        <input type='text' id='other-contact-info-input' placeholder='Другое' maxlength='100'><br/>
                        <hr/>
                    </div>

                    <button class='card' id='done-button' onclick='submitForm()'>Готово!</button>
                </div>

                <script>
                    function showInput(inputId) {{
                        const input = document.getElementById(inputId + "-input") || document.getElementById(inputId + "-textarea");
                        if (input) {{
                            input.style.display = (input.style.display === 'none') ? 'block' : 'none';
                        }}
                    }}

                    function showContactMe() {{
                        const contactContainer = document.getElementById("contact-me-container");
                        contactContainer.style.display = (contactContainer.style.display === "none") ? "block" : "none";
                    }}

                    function submitForm() {{
                        const username = document.getElementById("username").textContent.split("-")[1];
                        const nameValue = document.getElementById("name-input") ? (document.getElementById("name-input").value || null) : null;
                        const ageInput = document.getElementById("age-input");
                        const age = ageInput ? (ageInput.value || null) : null;
                        const hobbies = document.getElementById("hobbies-input").value || null;
                        const bio = document.getElementById("bio-textarea").value || null;

                        const telegram = document.getElementById("telegram-input").value || null;
                        const email = document.getElementById("email-input").value || null;
                        const phone = document.getElementById("phone-input").value || null;
                        const otherContactInfo = document.getElementById("other-contact-info-input").value || null;

                        // Check if age is valid
                        if (ageInput && !ageInput.checkValidity()) {{
                            alert("Пожалуйста, введите корректный возраст (от 1 до 150)");
                            return;
                        }}

                        const data = {{
                            username: username,
                            name: nameValue,
                            age: age,
                            hobbies: hobbies,
                            bio: bio,
                            telegram: telegram,
                            email: email,
                            phone: phone,
                            otherContactInfo: otherContactInfo
                        }};

                        fetch("http://127.0.0.1:8000/save_data", {{
                            method: "POST",
                            headers: {{
                                "Content-Type": "application/json"
                            }},
                            body: JSON.stringify(data)
                        }})
                        .then(response => {{
                            if (response.ok) {{
                                window.location.href = "http://127.0.0.1:8000";
                            }} else {{
                                alert("Ошибка при отправке данных");
                            }}
                        }})
                        .catch(error => console.error("Ошибка:", error));
                    }}
                </script>
            </body>
        </html>
        """

    return html_content
