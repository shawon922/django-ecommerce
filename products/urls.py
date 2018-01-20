from django.urls import path

from .views import ProductListView, ProductDetailView, create, update, delete, child_category

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('create/', create, name='create'),
    path('detail/<pk>/', ProductDetailView.as_view(), name='detail'),
    path('update/<pk>/', update, name='update'),
    path('delete/<pk>/', delete, name='delete'),
    path('subcategory/', child_category, name='subcategory'),
]
