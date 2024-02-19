from django.contrib import admin
from .models import Vehicle, VehicleImages
from django.utils.html import format_html


from PIL import Image

from django.utils.safestring import mark_safe





class VehicleImagesInline(admin.TabularInline):
    model = VehicleImages
    extra=0
    list_display = [
        "thumbnail",
    ]
    list_display_links = [
        "thumbnail"
    ]
    readonly_fields = [
        "thumbnail"
    ]

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="/media/{url}" width="75" height="auto" >'.format(
                    url=obj.image.url.split("/media/")[-1])
            )



class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        VehicleImagesInline
    ]



admin.site.register(Vehicle, VehicleAdmin)



