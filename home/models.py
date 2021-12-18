from django.db import models


class Contact(models.Model):
    contact_address = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50)


class Refunds(models.Model):

    class Meta:
        verbose_name_plural = 'Refunds'

    refund = models.TextField()


class Tandcs(models.Model):

    class Meta:
        verbose_name_plural = 'Tandcs'

    last_update = models.CharField(max_length=100)
    terms = models.TextField()


class Home_image(models.Model):
    image_url = models.URLField(max_length=200)
