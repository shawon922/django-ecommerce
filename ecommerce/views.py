from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from categories.models import Category
from products.models import Product

from time import time


def home(request):
    categories = Category.objects.prefetch_related('categories').filter(parent=None)

    queryset = Product.objects.select_related(
        'category__parent').all().order_by('category_id')

    # print(queryset)
    
    # start = time()

    products = {}

    for product in queryset:
        parent_category = product.category.parent.id

        try:
            if len(products[parent_category]) < 8:
                products[parent_category].append(product)
        except KeyError:
            products[parent_category] = []
            products[parent_category].append(product)

        # if parent_category not in products.keys():
        #     products[parent_category] = []
        # products[parent_category].append(product)
    
    # end = time()

    # print(end-start)

    # print(products)
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)


class CategoryWiseProductListView(ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 1
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        kwargs['categories'] = self.categories
        return super().get_context_data(*args, **kwargs)

    def get_queryset(self):
        self.categories = Category.objects.prefetch_related(
            'categories').filter(parent=None)

        request = self.request
        q = request.GET.get('q')
        print(q)
        
        category_id = self.kwargs.get('category_id')
        sub_category_id = self.kwargs.get('sub_category_id', None)

        if sub_category_id:
            queryset = Product.objects.filter(category=sub_category_id).order_by('-updated_at')
        else:
            queryset = Product.objects.filter(category__parent=category_id).order_by('-updated_at')

        return queryset


def products(request, category_id, sub_category_id=None):
    page_var = 'page'
    categories = Category.objects.prefetch_related('categories').filter(parent=None)

    if sub_category_id:
        queryset = Product.objects.filter(category=sub_category_id)
    else:
        queryset = Product.objects.filter(category__parent=category_id)
    # print(queryset)

    paginator = Paginator(queryset, 18)

    page = request.GET.get(page_var)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'products': products,
        'page_var': page_var,
    }

    return render(request, 'products.html', context)

def backend_home(request):
    return render(request, 'backend_home.html', {})
