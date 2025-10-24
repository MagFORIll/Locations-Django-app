from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpRequest
from .models import Location
from typing import Dict, Any




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
