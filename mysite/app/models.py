from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название локации')
    place_id = models.CharField(max_length=100, unique=True, verbose_name='ID локации')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    image = models.ImageField(upload_to='locations/', blank=True, null=True, verbose_name='Главное фото')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = models.TextField(blank=True, verbose_name='Длинное описание')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, ({self.place_id})'

    @property
    def geojson(self):
        return {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [self.longitude, self.latitude],
            },
            'properties': {
                'title': self.title,
                'placeId': self.id,
            },
        }


class LocationImage(models.Model):
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations/gallery/')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Подпись')

    class Meta:
        verbose_name = 'Фото локации'
        verbose_name_plural = 'Фото локаций'

    def __str__(self):
        return f'Фото для {self.location.title}'