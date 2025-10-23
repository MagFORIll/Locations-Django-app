from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Location



# Create your views here.
def locations_geojson(request):
    """Список всех локаций в Geojson"""
    features = [loc.geojson for loc in Location.objects.all()]
    return JsonResponse({'type': 'FeatureCollection', 'features': features})

def location_details(request, pk):
    """Подробные сведения о конкретной локации"""
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
