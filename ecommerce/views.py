from django.shortcuts import render

from categories.models import Category
from products.models import Product


def home(request):
    categories = Category.objects.filter(parent=None).all()

    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)


def backend_home(request):
    return render(request, 'backend_home.html', {})
