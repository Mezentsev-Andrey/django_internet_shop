from django.urls import path

from catalog.views import index, contacts


urlpatterns = [
    path('', index),
    path('catalog/contacts/', contacts)
]
