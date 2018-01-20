from django.shortcuts import render, redirect, get_object_or_404

from .models import Category 
from .forms import CategoryForm


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'categories/index.html', context)

def create(request):
    form = CategoryForm(request.POST or None)
    
    if form.is_valid():
        category = form.save(commit=False)

        category.save()

        return redirect('categories:index')

    context = {
        'form': form,
    }
    return render(request, 'categories/create.html', context)

def update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        category = form.save(commit=False)
        category.save()

        return redirect('categories:index')
    
    context = {
        'form': form,
    }
    return render(request, 'categories/update.html', context)
