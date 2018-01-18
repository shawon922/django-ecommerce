from django.shortcuts import render

from .forms import CategoryForm


def index(request):
    
    context = {
        
    }
    return render(request, 'categories/index.html', context)

def create(request):
    form = CategoryForm(request.POST or None)
    
    if form.is_valid():
        print(form.cleaned_data)
        
        category = form.save(commit=False)
        category.save()

    context = {
        'form': form,
    }
    return render(request, 'categories/create.html', context)
