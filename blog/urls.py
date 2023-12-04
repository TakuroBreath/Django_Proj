from django.urls import path

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='update'),
    path('detail/<slug>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='delete'),
]
