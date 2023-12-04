from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views += 1
        object.save()
        return object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:detail", args=[self.kwargs.get("slug")])


class BlogDeleteView(DeleteView):
    model = Blog

    success_url = reverse_lazy('blog:list')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()

        return super().form_valid(form)
