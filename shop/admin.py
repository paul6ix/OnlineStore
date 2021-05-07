from django.contrib import admin
from .models import ModelProduct, ModelCheckout

# Register your models here.
admin.site.register(ModelProduct)
admin.site.register(ModelCheckout)
