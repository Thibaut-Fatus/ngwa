from django.db import models


class EmptyClass(models.Model):
    """
    name
    url
    image
    """
    url = models.CharField(max_length=500, primary_key='True')
    name = models.CharField(max_length=30)
