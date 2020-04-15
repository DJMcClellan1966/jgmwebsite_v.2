from django.contrib import admin

from .models import Image

admin.site.register(Image)

class ImageAlbumAdmin(admin.ModelAdmin):
    fieldsets = (
    (None, {
        'fields': ('title', 'images')
    })
    )
