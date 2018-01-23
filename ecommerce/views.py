from django.shortcuts import render

from categories.models import Category
from products.models import Product


def home(request):
    categories = Category.objects.prefetch_related('categories').filter(parent=None).all()

    queryset = Product.objects.select_related(
        'category__parent').all().order_by('category_id')

    products = {}

    for product in queryset:
        parent_category = product.category.parent.id
        products[parent_category] = []
        products[parent_category].append(product)
    
    print(products[1])        
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)


def backend_home(request):
    return render(request, 'backend_home.html', {})
