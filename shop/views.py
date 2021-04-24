from django.shortcuts import render
from .models import ModelProduct


# Create your views here.

def product_views(request):
    products = ModelProduct.objects.all()
    # Creating a search function for the index page, the name of the input form must march the get
    product_search = request.GET.get('product_search')
    if product_search != '' and product_search is not None:
        # filter with one of your models
        products = products.filter(product_name__icontains=product_search)

    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)
