from fastapi import APIRouter
from starlette.responses import HTMLResponse

showing_questionnaires = APIRouter()


@showing_questionnaires.get("/showing_questionnaires", response_class=HTMLResponse)
def html_landing():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Анкеты пользователей</title>
        <style>
            /* Общие стили */
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: flex-start; /* Смещаем контент влево */
                justify-content: center;
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd'); /* Ваша картинка на фоне */
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }

            /* Контейнер для карточек и пагинации */
            #content-container {
                margin-left: 200px; /* Смещаем контент вправо на 200 пикселей */
                width: 80%;
                max-width: 600px;
            }

            /* Контейнер для карточек */
            #users-container {
                display: flex;
                flex-direction: column;
                align-items: flex-start; /* Карточки смещены влево */
            }

            /* Стили карточки */
            .user-card {
                background: rgba(30, 30, 30, 0.9); /* Темный фон карточки с прозрачностью */
                padding: 20px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                width: 100%;
                cursor: pointer; /* Курсор указывает, что карточку можно нажать */
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                color: #ffffff; /* Белый текст */
            }

            /* Анимация при наведении на карточку */
            .user-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5);
            }

            /* Заголовок карточки (имя пользователя) */
            .user-card h3 {
                margin: 0;
                font-size: 1.5em;
            }

            /* Основной текст (возраст) */
            .user-card p {
                margin: 5px 0;
                font-size: 1em;
                color: #cccccc; /* Светло-серый текст */
            }

            /* Дополнительные поля (скрыты по умолчанию) */
            .user-card .details {
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.2s ease-in-out; /* Уменьшили время анимации */
                margin-top: 10px;
            }

            .user-card.open .details {
                max-height: 500px; /* или другое подходящее значение */
            }

            /* Отступ после "О себе" */
            .user-card .details p:nth-of-type(2) {
                margin-bottom: 20px;
            }

            /* Отступы перед и после "Другое" */
            .user-card .details p:nth-of-type(6) {
                margin-top: 20px;
                margin-bottom: 20px;
            }

            /* Стили для кнопок пагинации */
            .pagination {
                margin-top: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }

            .pagination button {
                background: rgba(30, 30, 30, 0.9); /* Темный фон кнопок */
                color: #ffffff; /* Белый текст */
                border: none;
                padding: 10px 15px;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.2s ease;
            }

            .pagination button:hover {
                background: rgba(50, 50, 50, 0.9); /* Светлее при наведении */
            }

            .pagination button:disabled {
                background: rgba(70, 70, 70, 0.9); /* Серый для неактивных кнопок */
                cursor: not-allowed;
            }

            /* Текст пагинации (номер страницы и слово "Страница") */
            .pagination #page-info {
                font-weight: bold; /* Жирный текст */
                color: #ffffff; /* Белый текст */
            }

            /* Стрелка для раскрытия карточки */
            .user-card .arrow {
                float: right;
                font-size: 1.2em;
                transition: transform 0.2s ease; /* Уменьшили время анимации */
            }

            .user-card.open .arrow {
                transform: rotate(180deg); /* Поворачиваем стрелку при раскрытии */
            }

            /* Стили для отображения текста в две строки */
            .details p.multiline {
                white-space: pre-wrap; /* Отображение переносов строк и пробелов */
                word-break: break-word; /* Перенос слов, если они не помещаются */
            }

        </style>
    </head>
    <body>
        <!-- Контейнер для карточек и пагинации -->
        <div id="content-container">
            <!-- Контейнер для карточек -->
            <div id="users-container"></div>

            <!-- Пагинация -->
            <div class="pagination">
                <button id="prev-page">Назад</button>
                <span id="page-info">Страница 1</span>
                <button id="next-page">Вперед</button>
            </div>
        </div>

        <script>
            let currentPage = 1;
            let totalPages = 1; // Добавим переменную для хранения общего количества страниц

            // Функция для загрузки данных с бэкенда
            async function fetchUsers(page) {
                const response = await fetch(`/get_all_users_data?page=${page}&limit=2`);
                const data = await response.json();
                return data;
            }

            // Функция для разделения текста на строки
            function splitText(text, maxLength) {
                if (!text) {
                    return "";
                }

                const words = text.split(" ");
                let lines = [];
                let currentLine = "";

                for (const word of words) {
                    if (currentLine.length > 0 && currentLine.length + word.length + 1 > maxLength) {
                        lines.push(currentLine);
                        currentLine = word;
                    } else {
                        currentLine = currentLine ? `${currentLine} ${word}` : word;
                    }
                }

                lines.push(currentLine);
                return lines.join("\\n"); // Используем перенос строки для pre-wrap
            }

            // Функция для отображения карточек
            function renderUsers(users) {
                const container = document.getElementById('users-container');
                container.innerHTML = users.map(user => {
                    const bioLines = splitText(user.bio, 50);
                    const otherLines = splitText(user.other, 50);

                    // Функция для замены null на "Не заполнено" курсивом
                    const replaceNull = (value) => {
                        if (value === null || value === undefined || value === '') {
                            return '<i>Не заполнено</i>';
                        }
                        return value;
                    };

                    return `
                        <div class="user-card" onclick="toggleDetails(this)">
                            <h3>${replaceNull(user.username)}</h3>
                            <p>Возраст: ${replaceNull(user.age)}</p>
                            <div class="details">
                                <p>Хобби: ${replaceNull(user.hobbies)}</p>
                                <p class="multiline">О себе: ${replaceNull(bioLines)}</p>
                                <p>Телеграм: ${replaceNull(user.telegram)}</p>
                                <p>Email: ${replaceNull(user.email)}</p>
                                <p>Телефон: ${replaceNull(user.phone)}</p>
                                <p class="multiline">Другое: ${replaceNull(otherLines)}</p>
                                <p>Создано: ${new Date(user.created_at).toLocaleString()}</p>
                            </div>
                            <span class="arrow">▼</span>
                        </div>
                    `;
                }).join('');
            }

            // Функция для обновления пагинации
            function updatePagination(page, total) {
                const limit = 2; // Количество анкет на странице
                totalPages = Math.ceil(total / limit); // Вычисляем общее количество страниц

                document.getElementById('page-info').textContent = `Страница ${page} / ${totalPages}`;
                document.getElementById('prev-page').disabled = page === 1;

                // Проверяем, есть ли записи на следующей странице
                document.getElementById('next-page').disabled = page === totalPages || totalPages === 0;
            }

            // Функция для загрузки страницы
            async function loadPage(page) {
                const data = await fetchUsers(page);
                renderUsers(data.users);
                updatePagination(page, data.total);
            }

            // Функция для раскрытия/скрытия деталей карточки
            function toggleDetails(card) {
                const details = card.querySelector('.details');

                // Закрываем все открытые анкеты, кроме текущей
                document.querySelectorAll('.user-card.open').forEach(openCard => {
                    if (openCard !== card) {
                        const openDetails = openCard.querySelector('.details');
                        openCard.classList.remove('open');
                        openDetails.style.maxHeight = '0';
                    }
                });

                if (card.classList.contains('open')) {
                    // Если анкета открыта, сначала закрываем ее
                    details.style.maxHeight = '0';
                    card.classList.remove('open');
                } else {
                    // Если анкета закрыта, открываем ее
                    card.classList.add('open');
                    details.style.maxHeight = '500px';
                }
            }

            // Обработчики кнопок пагинации
            document.getElementById('prev-page').addEventListener('click', () => {
                if (currentPage > 1) {
                    currentPage--;
                    loadPage(currentPage);
                }
            });

            document.getElementById('next-page').addEventListener('click', () => {
                if (currentPage < totalPages) {
                    currentPage++;
                    loadPage(currentPage);
                }
            });

            // Загружаем первую страницу при загрузке
            loadPage(currentPage);
        </script>
    </body>
    </html>
    """
