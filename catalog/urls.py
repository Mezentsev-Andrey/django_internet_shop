from django.urls import path

from catalog.views import index, contacts, product_info, product_list

app_name = 'catalog_product'

urlpatterns = [
    path('', index),
    path('catalog/contacts/', contacts),
    path('', product_list, name='all_products'),
    path('<int:pk>/', product_info,name='product_info'),
]
