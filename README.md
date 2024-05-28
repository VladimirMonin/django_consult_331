# Проект Python Telegram Bot с бэкэндом на Django

## Описание проекта

Этот проект представляет собой веб-сайт с визиткой и формой записи на консультацию, разработанный с использованием Django и библиотеки Python Telegram Bot. Веб-сайт включает функционал для записи пользователей на консультации, а также возможностью управления записями через личный кабинет (планируется добавить в будущем). Проект использует базу данных SQLite, Django CrispyForm для улучшенного рендеринга форм и Bootstrap 5 для стилизации. Также используются Django сигналы для обработки событий в приложении.

## Технологии

- **Django**: основной фреймворк для веб-приложения. `pip install django`
- **SQLite**: база данных для хранения информации о пользователях и записях на консультацию. 
- **CrispyForm**: библиотека для улучшенного рендеринга Django форм. `pip install django-crispy-forms`
- **Bootstrap 5**: CSS-фреймворк для стилизации. 
- **Python Telegram Bot**: библиотека для взаимодействия с Telegram API. `pip install python-telegram-bot`
- **Django сигналы**: для обработки событий и взаимодействия между компонентами приложения.

## Установка и запуск проекта

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Скопируйте файл `.env.example` и переименуйте его в `.env`:
    ```bash
    cp .env.example .env
    ```

5. Откройте файл `.env` и заполните следующие переменные окружения:
    - `DJANGO_SECRET_KEY`: секретный ключ Django.
    - `TELEGRAM_BOT_API_KEY`: API-ключ вашего Telegram-бота.

6. Примените миграции:
    ```bash
    python manage.py migrate
    ```

7. Создайте суперпользователя для доступа к админ-панели Django:
    ```bash
    python manage.py createsuperuser
    ```

8. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## История коммитов

История коммитов будет содержать подробные описания изменений, внесенных в проект, для обеспечения прозрачности и удобства отслеживания прогресса.

### Шаблон для описания коммитов:

1. **Описание**:
    - Подробное описание внесенных изменений.
    - Причины внесения изменений.
    - Любые важные заметки или инструкции по использованию новых функций.

2. **Заголовок**: Краткое описание изменений (максимум 50 символов).


---

### Подготовка проекта

**Описание**:
Установили зависимости для проекта.
`pip install django`
`pip install django-crispy-forms`
`pip install crispy-bootstrap5`
`pip install python-telegram-bot`

Сохранили их в файл `requirements.txt`.
`pip freeze > requirements.txt`

Создали виртуальное окружение и активировали его.

Создали README.md файл и добавили описание проекта.

Создали Джанго проект и приложение `consultations`.

`django-admin startproject consultations .`
`python manage.py startapp consultations_app`

**Заголовок**: `init: подготовка проекта`

---
**Описание**:
### Работа с шаблонами

На текущий момент проект предусматривает 3 шаблона:

- `base.html`: базовый шаблон для всех страниц.
- `main.html`: главная страница сайта.
- `thank_you.html`: страница благодарности за запись на консультацию.

Предварительная структура проекта

```csharp
consult/
├── consult/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── static/
│   └── images/
│       └── photo.jpg
├── templates/
│   ├── base.html
│   ├── main.html
│   └── thank_you.html
├── manage.py
└── ...
```

Добавил папку static для хранения статических файлов (картинки, стили, скрипты).
В ней сделал папку `images` и добавил туда фото для главной страницы.
Подключил папку static в файле `settings.py`.

Подключил CryspyForm в файле `settings.py`.
```python

INSTALLED_APPS = [
    ...
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```
**Заголовок**: `feat: добавил шаблоны`
---

**Описание**:
### Тестовый запуск

Создал View(TemplateView) для главной страницы сайта.
Добавил URL-паттерн для главной страницы.

Но мы получили TemplateDoesNotExist
Необходимо внести в файл `settings.py` путь к папке с шаблонами.

```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

**Заголовок**: `fix: исправил ошибку TemplateDoesNotExist`
---

**Описание**:
### Создание модели

`ConsultationRequest` - модель для хранения информации о пользователях, записавшихся на консультацию.


Пофиксил CryspyForm BS5
Надо было установить еще один пакет и добавить его в INSTALLED_APPS
Установил https://pypi.org/project/crispy-bootstrap5/
`pip install crispy-bootstrap5`
Добавил в INSTALLED_APPS `crispy_bootstrap5`

**Заголовок**: `fix: исправил CryspyForm BS5 и добавил модель`

---

**Описание**:
Исправил 2 косяка, из-за чего приложение не работало.
1. В урлах страница благодарности имела тот же адрес, что и главная страница.
2. В модели `ConsultationRequest` показывал метод save, который не в итоге не вызвал save родителя и ничего не сохранял.

**Заголовок**: `fix: исправил косяки`