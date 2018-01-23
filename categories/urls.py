from django.urls import path

from .views import CategoryListView, create, update

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('create/', create, name='create'),
    path('update/<pk>/', update, name='update'),
]
