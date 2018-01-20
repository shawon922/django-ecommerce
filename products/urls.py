from django.urls import path

from .views import index, create, update, delete, child_category

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<pk>/', update, name='update'),
    path('delete/<pk>/', delete, name='delete'),
    path('subcategory/', child_category, name='subcategory'),
]
