from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название локации')
    place_id = models.CharField(max_length=100, unique=True, verbose_name='ID локации')
    details_url = models.URLField(verbose_name='URL для сведений (JSON)')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, ({self.place_id})'