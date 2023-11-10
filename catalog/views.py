from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def main(request):
    return render(request, 'catalog/main.html')


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Categories',
    }
    return render(request, 'catalog/categories.html', context)


def products(request, pk):
    content = Category.objects.filter(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'{content}',
    }
    return render(request, 'catalog/products.html', context)
