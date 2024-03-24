from django.urls import path

from catalog.views import ProductListView, ProductView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='list_products'),
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    ]
