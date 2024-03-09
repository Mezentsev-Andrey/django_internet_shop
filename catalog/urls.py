from django.urls import path

from catalog.views import home, contacts, product_info, product_catalog

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', product_info, name='product_info'),
    path('product_catalog/', product_catalog, name='product_catalog'),
]
