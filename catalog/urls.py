from django.urls import path

from catalog.views import ProductListView, ProductView, ProductDetailView

app_name = 'shop'

#home, contacts, product_info, product_catalog,

# urlpatterns = [
#     path('', home, name='home'),
#     path('contacts/', contacts, name='contacts'),
#     path('<int:pk>/', product_info, name='product_info'),
#     path('product_catalog/', product_catalog, name='product_catalog'),
# ]

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    ]
