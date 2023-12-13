from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, ProductListView, CategoryListView, ProductCreateView, VersionCreateView, \
    VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/create_version/', VersionCreateView.as_view(), name='create_version'),
    path('product/version/<int:pk>/update/', VersionUpdateView.as_view(), name='update_version'),
]
