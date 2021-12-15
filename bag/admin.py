from django.contrib import admin
from .models import Bag


class BagAdmin(admin.ModelAdmin):
    list_display = (
        'bag_message',
    )


admin.site.register(Bag, BagAdmin)
