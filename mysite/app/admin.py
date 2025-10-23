from django.contrib import admin
from .models import Location, LocationImage

# Register your models here.
class LocationImageInline(admin.TabularInline):
    model = LocationImage
    extra = 1

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_id', 'latitude', 'longitude')
    search_fields = ('title', 'place_id')
    list_filter = ('title',)
    inlines = [LocationImageInline]

