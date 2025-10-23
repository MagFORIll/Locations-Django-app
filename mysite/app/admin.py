from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Location, LocationImage
from django.utils.html import mark_safe

# Register your models here.
class LocationImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = LocationImage
    extra = 0
    readonly_fields = ('image_preview',)
    fields = ('image_preview', 'image', 'caption')
    show_change_link = False
    ordering = ('position',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" style="object-fit: cover; border-radius: 6px;" />')
        return '-'
    image_preview.short_description = 'Превью'

@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'place_id')
    readonly_fields = ('image_preview', )
    inlines = [LocationImageInline]

