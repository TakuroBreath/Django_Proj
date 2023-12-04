from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Product


def main(request):
    return render(request, 'catalog/main.html')


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


