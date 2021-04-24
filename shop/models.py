from django.db import models
from django import forms


# Create your models here.
class ModelProduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_type = models.CharField(max_length=250)
    product_desc = models.TextField()
    Product_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_name
