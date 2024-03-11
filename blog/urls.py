from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
     path('create/', BlogCreateView.as_view(), name='create'),
     path('', BlogListView.as_view(), name='blog_list'),
     path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
     path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
     path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
