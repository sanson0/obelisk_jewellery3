from django.db import models


class Bag(models.Model):
    bag_message = models.CharField(max_length=100)
