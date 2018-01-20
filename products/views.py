from django.shortcuts import render, redirect, get_object_or_404
from django.http import response

from categories.models import Category
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


def create(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        # cd = form.cleaned_data
        # category = cd.get('category')
        # name = cd.get('name')
        # description = cd.get('description')
        # price = cd.get('price')

        # Product.objects.create(category=category, name=name, description=description, price=price)
        # product = Product(category=category, name=name, description=description, price=price)

        product = form.save(commit=False)
        product.save()

        return redirect('products:index')

    context = {
        'form': form,
    }

    return render(request, 'products/create.html', context)


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # sub_category = product.category
    product.sub_category = product.category
    if product.category.parent:
        product.category = product.category.parent
    else:
        product.category = product.category

    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()

        return redirect('products:index')
    context = {
        'form': form,
    }
    return render(request, 'products/update.html', context)


def delete(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products:index')
    else:
        return response.HttpResponseNotAllowed(permitted_methods=['post'])


def child_category(request):
    if request.method == 'POST':
        parent = request.POST.get('parent')
        category_list = list(Category.objects.filter(parent=parent).values('id', 'name'))
        # print(category_list)
        return response.JsonResponse(category_list, safe=False)
    else:
        return response.HttpResponseNotAllowed(permitted_methods=['post'])
