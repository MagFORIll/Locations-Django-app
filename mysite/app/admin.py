from django.contrib import admin
from .models import Location, LocationImage
from django.utils.html import mark_safe

# Register your models here.
class LocationImageInline(admin.TabularInline):
    model = LocationImage
    extra = 1
    readonly_fields = ('image_preview',)
    field = ('image_preview', 'image', 'caption')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" style="object-fit: cover; border-radius: 6px;" />')
    image_preview.short_description = 'Превью'

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_id', 'latitude', 'longitude')
    search_fields = ('title', 'place_id')
    list_filter = ('title',)
    readonly_fields = ('image_preview', )
    inlines = [LocationImageInline]

