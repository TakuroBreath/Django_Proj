from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.models import Category, Product, Version
from catalog.services import cache_categories


def main(request):
    return render(request, 'catalog/main.html')


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = cache_categories()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.description)
            new_form.user = self.request.user
            new_form.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:categories')


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:categories')


class ProductDetailView(DetailView):
    model = Product
