from django.contrib import admin
from .models import Location

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_id', 'details_url')
    search_fields = ('title', 'place_id')
    list_filter = ('title',)

