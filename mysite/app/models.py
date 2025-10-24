from django.db import models
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Location(models.Model):
    """
    Модель локации с геокоординатами и описанием.

    Attributes:
        title (str): Название локации.
        place_id (str): Уникальный идентификатор.
        latitude (float): Широта.
        longitude (float): Долгота.
        image (ImageField): Главное фото.
        description_short (str): Короткое описание.
        description_long (str): Полное описание.
    """
    title = models.CharField(max_length=255, verbose_name='Название локации')
    place_id = models.CharField(max_length=100, unique=True, verbose_name='ID локации')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    image = models.ImageField(upload_to='locations/', blank=True, null=True, verbose_name='Главное фото')
    description_short = RichTextUploadingField(blank=True, verbose_name='Короткое описание')
    description_long = RichTextUploadingField(blank=True, verbose_name='Длинное описание')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, ({self.place_id})'

    @property
    def geojson(self):
        """Возвращает представление локации в формате GeoJSON."""
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

    def image_preview(self):
        """Отображает миниатюру главного изображения в админке."""
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" style="object-fit: cover; border-radius: 8px;" />')
        return '-'
    image_preview.short_description = 'Превью'


class LocationImage(models.Model):
    """
    Дополнительные изображения для локации (галерея).

    Attributes:
        location (Location): Родительская локация.
        image (ImageField): Изображение.
        caption (str): Подпись.
        position (int): Порядок сортировки.
    """
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations/gallery/')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Подпись')
    position = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Фото локации'
        verbose_name_plural = 'Фото локаций'
        ordering = ['position']

    def __str__(self):
        return f'Фото для {self.location.title}'