from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, ProductListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('/products/<int:pk>/', ProductListView.as_view(), name='products'),
]
