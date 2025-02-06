from fastapi import Request, APIRouter
from starlette.responses import HTMLResponse


questionnaire_router = APIRouter()


@questionnaire_router.get("/questionnaire", response_class=HTMLResponse)
def html_landing():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Анкета</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                align-items: center; /* Центрирование по вертикали */
                justify-content: center; /* Центрирование по горизонтали */
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }
            .container {
                text-align: center; /* Центрирование содержимого */
            }
            .card {
                padding: 20px 40px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
                cursor: pointer;
            }
            .black-card {
                color: white;
                background-color: black;
                border: none;
            }
            #contact-me-container {
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div id="username">Имя - example_name</div>
            <button class="card black-card" onclick="showAgeInput()">Возраст</button>
            <input type="number" id="age-input" min="1" max="150" placeholder="Введите возраст" style="display:none;" required>
            <button class="card black-card" onclick="showHobbiesInput()">Хобби</button>
            <input type="text" id="hobbies-input" maxlength="50" placeholder="Введите хобби" style="display:none;">
            <textarea id="bio-textarea" rows="5" cols="30" maxlength="100" placeholder="О себе"></textarea><br/>
            <button class="card black-card" onclick="showContactMe()">Связаться со мной</button><br/>
            <div id="contact-me-container">
                <input type="text" id="telegram-input" placeholder="Телеграмм (до 50 символов)" maxlength="50"><br/><br/>
                <input type="email" id="email-input" placeholder="Email (до 50 символов)" maxlength="50"><br/><br/>
                <input type="tel" id="phone-input" placeholder="Телефон (до 30 символов)" maxlength="30"><br/><br/>
                <input type="text" id="other-contact-info-input" placeholder="Другое (до 30 символов)" maxlength="30">
            </div>
            <button class="card black-card" onclick="submitForm()">Готово!</button>
        </div>
        <script>
            function showAgeInput() {
                const ageInput = document.getElementById("age-input");
                ageInput.style.display = ageInput.style.display === "none" ? "block" : "none";
            }
            function showHobbiesInput() {
                const hobbiesInput = document.getElementById("hobbies-input");
                hobbiesInput.style.display = hobbiesInput.style.display === "none" ? "block" : "none";
            }
            function showContactMe() {
                const contactContainer = document.getElementById("contact-me-container");
                contactContainer.style.display = contactContainer.style.display === "none" ? "block" : "none";
            }
            function submitForm() {
                const username = document.getElementById("username").textContent.split(" - ")[1];
                const age = document.getElementById("age-input").value || null;

                if (!age) { // Проверка на обязательность возраста
                    alert("Пожалуйста, укажите ваш возраст.");
                    return;
                }

                const hobbies = document.getElementById("hobbies-input").value || null;
                const bio = document.getElementById("bio-textarea").value || null;
                const telegram = document.getElementById("telegram-input").value || null;
                const email = document.getElementById("email-input").value || null;
                const phone = document.getElementById("phone-input").value || null;
                const otherContactInfo = document.getElementById("other-contact-info-input").value || null;

                fetch("/save_data", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        username,
                        age,
                        hobbies,
                        bio,
                        telegram,
                        email,
                        phone,
                        otherContactInfo
                    })
                }).then(response => {
                    if (response.ok) {
                        window.location.href = "https://GGGGGGGGGGG";
                    } else {
                        alert("Ошибка при отправке данных");
                    }
                }).catch(error => console.error("Ошибка:", error));
            }
        </script>
    </body>
    </html>
    """


@questionnaire_router.post(path="/save_data", status_code=201)
async def save_data(request: Request):
    form_data = await request.json()

    print({
        "Имя": form_data["username"],
        "Возраст": form_data["age"],
        "Хобби": form_data["hobbies"],
        "О себе": form_data["bio"],
        "Телеграмм": form_data["telegram"],
        "Email": form_data["email"],
        "Телефон": form_data["phone"],
        "Другое": form_data["otherContactInfo"]
    })

    return {"message": f"{form_data['username']}'s data saved successfully"}
