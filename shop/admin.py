from django.contrib import admin
from .models import ModelProduct, ModelCheckout


# Register your models here.
class OrderDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'city', 'items', 'total')
    search_fields = ('name',)


admin.site.register(ModelProduct)
admin.site.register(ModelCheckout, OrderDetails)

admin.site.site_header = "Shop Manager"
admin.site.site_title = "Admin Backend"
