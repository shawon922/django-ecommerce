from django.urls import path

from .views import index, create

app_name = 'categories'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
]
