from django.urls import path

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

# urlpatterns = [
#     path('', main, name='main'),
#     path('categories/', CategoryListView.as_view(), name='categories'),
#     path('/products/<int:pk>/', ProductListView.as_view(), name='products'),
# ]
