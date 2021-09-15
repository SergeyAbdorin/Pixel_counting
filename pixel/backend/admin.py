from django.contrib import admin

from .models import ImageModel, PixelCount


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ("image", "id", "upload_date")
    search_fields = ("upload_date",)
    list_filter = ("upload_date",)
    empty_value_display = "-пусто-"


class PixelCountAdmin(admin.ModelAdmin):
    list_display = ("image", "id", "image_id")
    search_fields = ("colors",)
    list_filter = ("image",)
    empty_value_display = "-пусто-"


admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(PixelCount, PixelCountAdmin)
