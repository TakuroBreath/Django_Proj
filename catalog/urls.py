from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import main, ProductListView, CategoryListView, ProductCreateView, VersionCreateView, \
    VersionUpdateView, CategoryCreateView, ProductUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', (ProductListView.as_view()), name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(template_name='catalog/product_update.html'), name='update'),
    path('product/<int:pk>/create_version/', VersionCreateView.as_view(), name='create_version'),
    path('product/version/<int:pk>/update/', VersionUpdateView.as_view(), name='update_version'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
]
