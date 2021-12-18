from django.contrib import admin
from .models import Bag


class BagAdmin(admin.ModelAdmin):
    list_display = (
        'bag_message',
        'image_url',
        'image_description',
        'promotion',
    )


admin.site.register(Bag, BagAdmin)
