from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


def main(request):
    return render(request, 'catalog/main.html')


class CategoryListView(ListView):
    model = Category


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.user = self.request.user
            new_form.save()

        return super().form_valid(form)


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:categories')


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
