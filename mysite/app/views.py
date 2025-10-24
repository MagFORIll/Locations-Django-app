import os.path

from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from .models import Location, LocationImage
from django.core.files import File
from mysite.settings import MEDIA_ROOT
from typing import Dict, Any

from ..mysite.settings import MEDIA_ROOT


# Create your views here.
def locations_geojson(request: HttpRequest) -> JsonResponse:
    """
    Возвращает список всех локаций в формате GeoJSON.

    Args:
        request (HttpRequest): HTTP-запрос от клиента.

    Returns:
        JsonResponse: Список всех локаций в формате GeoJSON.
    """
    features = [loc.geojson for loc in Location.objects.all()]
    return JsonResponse({'type': 'FeatureCollection', 'features': features})

def location_details(request: HttpRequest, pk: int) -> JsonResponse:
    """
    Возвращает подробную информацию о конкретной локации.

    Args:
        request (HttpRequest): HTTP-запрос от клиента.
        pk (int): Идентификатор локации (первичный ключ).

    Raises:
        Http404: Если локация с таким pk не найдена.

    Returns:
        JsonResponse: Подробные данные о локации.
    """
    try:
        loc = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        raise Http404('Локация не найдена')
    imgs = [loc.image.url] if loc.image else []
    imgs += [img.image.url for img in loc.images.all()]
    return JsonResponse({
        'title': loc.title,
        'placeId': loc.place_id,
        'imgs': imgs,
        'description_short': loc.description_short,
        'description_long': loc.description_long,
    })

def load_locations_from_json(json_path: str) -> None:
    """
    Импортирует локации из JSON-файла.

    Для каждой записи создаётся или обновляется объект Location и
    загружаются изображения (главное и галерея).

    Args:
        json_path (str): Абсолютный или относительный путь к JSON-файлу.

    Returns:
        None
    """
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        place_id = item.get('place_id')
        if not place_id:
            continue
        location, created = Location.objects.get_or_create(
            place_id=place_id,
            defaults={
                'title': item.get('title', ''),
                'latitude': item.get('latitude', 0.0),
                'longitude': item.get('longitude', 0.0),
                'description_short': item.get('description_short', ''),
                'description_long': item.get('description_long', '')
            }
        )

        main_image_path = item.get('image')
        if main_image_path:
            full_path = os.path.join(MEDIA_ROOT, main_image_path)
            if os.path.exists(full_path):
                with open(full_path, 'rb') as img_file:
                    location.image.save(os.path.basename(main_image_path), File(img_file), save=True)

        gallery = item.get('gallery', [])
        for img_path in gallery:
            full_path = os.path.join(MEDIA_ROOT, img_path)
            if os.path.exists(full_path):
                with open(full_path, 'rb') as img_file:
                    LocationImage.objects.create(
                        location=location,
                        image=File(img_file, name=os.path.basename(img_path))
                    )

        print(f"{'Создана' if created else 'Обновлена'} локация: {location.title}")