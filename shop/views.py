from django.shortcuts import render
from .models import ModelProduct
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Create your views here.

def product_views(request):
    products = ModelProduct.objects.all()
    # Creating a search function for the index page, the name of the input form must march the get
    product_search = request.GET.get('product_search')
    if product_search != '' and product_search is not None:
        # filter with one of your models
        products = products.filter(product_name__icontains=product_search)
    # creating a paginator function here
    # set the number of products per page
    pagination = Paginator(products, 3)
    # getting the set name from the html template
    pages = request.GET.get('page')
    # setting page to march context
    products = pagination.get_page(pages)
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


class ClassDetailView(DetailView):
    model = ModelProduct
    template_name = 'shop/product_detail.html'
    context_object_name = 'detail'
