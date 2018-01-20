from django.urls import path

from .views import index, create, update

app_name = 'categories'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<pk>/', update, name='update'),
]
