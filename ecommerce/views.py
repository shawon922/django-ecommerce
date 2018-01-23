from django.shortcuts import render

from categories.models import Category
from products.models import Product

from time import time


def home(request):
    categories = Category.objects.prefetch_related('categories').filter(parent=None).all()

    queryset = Product.objects.select_related(
        'category__parent').all().order_by('category_id')

    # print(queryset)
    
    start = time()

    products = {}

    for product in queryset:
        parent_category = product.category.parent.id

        try:
            products[parent_category].append(product)
        except KeyError:
            products[parent_category] = []
            products[parent_category].append(product)

        # if parent_category not in products.keys():
        #     products[parent_category] = []
        # products[parent_category].append(product)
    
    end = time()

    print(end-start)

    print(products)        
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)


def backend_home(request):
    return render(request, 'backend_home.html', {})
