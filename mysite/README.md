# GeoLocations Django App

Мини-проект для отображения интерактивных локаций с описанием, галереей и API на Django.

## Возможности
- Панель администратора с drag-and-drop сортировкой изображений.
- Поддержка WYSIWYG-редактора (CKEditor).
- REST API эндпоинты для фронтенда (GeoJSON + подробности локаций).
- Превью изображений в админке.
- Готово к деплою (используются переменные окружения).

---

## Установка и запуск

```bash
git clone https://github.com/MagFORIll/Test.git
cd mysite
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```
## API эндпоинты
Метод	URL	Описание
GET	/api/locations/	Возвращает список всех локаций (GeoJSON)
GET	/api/locations/<id>/	Возвращает подробные данные о конкретной локации

### Пример ответа:
---
json
{
  "title": "Тауэрский мост",
  "placeId": "tower_bridge",
  "imgs": ["/media/locations/tower.jpg"],
  "description_short": "<p>Краткое описание...</p>",
  "description_long": "<p>Подробное описание...</p>"
}
---
## Переменные окружения (.env)
#### env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
---
## Технологии
Django 5.x
CKEditor
adminsortable2
Pillow
python-dotenv
 
## Автор
Maks
Начинающий Python Backend-разработчик.
Работает с Flask, Django, SQLAlchemy, REST API и тестированием.
---