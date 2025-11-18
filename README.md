# Locations — Django App

Мини-проект для отображения **интерактивных локаций с картой, описанием, галереей и API** на Django.
---

##  Возможности

*  Отображение локаций на интерактивной карте (GeoJSON).
*  REST API для фронтенда (GeoJSON + детальная информация).
*  Галерея изображений с drag-and-drop сортировкой.
*  Поддержка **WYSIWYG-редактора** (CKEditor).
*  Превью изображений прямо в админке.
*  Поддержка `.env` — готово к деплою на сервер.

---

## Установка и запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/MagFORIll/Locations-Django-app.git
cd mysite

# 2. Создаём виртуальное окружение
python -m venv .venv
source .venv/bin/activate        # для Linux / macOS
# или
.venv\Scripts\activate           # для Windows

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Создаём и настраиваем .env
cp .env.example .env

# 5. Применяем миграции
python manage.py migrate

# 6. Запускаем сервер
python manage.py runserver
```

После запуска проект будет доступен по адресу:
 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API эндпоинты

| Метод | URL                    | Описание                                           |
| :---- | :--------------------- | :------------------------------------------------- |
| `GET` | `/api/locations/`      | Возвращает список всех локаций (в формате GeoJSON) |
| `GET` | `/api/locations/<id>/` | Возвращает подробные данные о конкретной локации   |

### Пример ответа

```json
{
  "title": "Тауэрский мост",
  "placeId": "tower_bridge",
  "imgs": ["/media/locations/tower.jpg"],
  "description_short": "<p>Краткое описание...</p>",
  "description_long": "<p>Подробное описание...</p>"
}
```

---

## Переменные окружения (.env)

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```
## Технологии

* **Django 5.x**
* **django-ckeditor**
* **django-admin-sortable2**
* **Pillow**
* **python-dotenv**

---
