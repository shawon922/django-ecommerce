from django.urls import path

from .views import ProductListView, ProductFeaturedListView, ProductDetailView, create, update, delete, child_category

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('featured/', ProductFeaturedListView.as_view(), name='featured_index'),
    path('create/', create, name='create'),
    path('detail/<slug>/', ProductDetailView.as_view(), name='detail'),
    path('update/<slug>/', update, name='update'),
    path('delete/<slug>/', delete, name='delete'),
    path('subcategory/', child_category, name='subcategory'),
]
