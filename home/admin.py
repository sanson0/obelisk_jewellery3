from django.contrib import admin
from .models import Contact, Refunds, Tandcs, Home_image


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_address',
        'contact_phone',
    )


class RefundsAdmin(admin.ModelAdmin):
    list_display = (
        'refund',
    )


class TandcsAdmin(admin.ModelAdmin):
    list_display = (
        'last_update',
        'terms',
    )


class Home_imageAdmin(admin.ModelAdmin):
    list_display = (
        'image_url',
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(Refunds, RefundsAdmin)
admin.site.register(Tandcs, TandcsAdmin)
admin.site.register(Home_image, Home_imageAdmin)
