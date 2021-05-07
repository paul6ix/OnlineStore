from django.shortcuts import render
from .models import ModelProduct, ModelCheckout
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


def checkout_view(request):
    # Another way of getting data from forms and saving into database, this is the third method i have seen.
    # it is easy to understand and use and gives more control but longer to code
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        total = request.POST.get('total', "")
        checkout = ModelCheckout(name=name, email=email, address=address, city=city, items=items, total=total)
        checkout.save()
    return render(request, 'shop/checkout.html')
