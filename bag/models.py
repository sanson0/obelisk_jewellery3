from django.db import models


class Bag(models.Model):
    bag_message = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, null=True)
    image_description = models.CharField(max_length=100, null=True)
    promotion = models.CharField(max_length=250, null=True)
