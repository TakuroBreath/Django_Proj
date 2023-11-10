from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, products, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', products, name='products'),
]
