from django.shortcuts import render

from catalog.models import Product, Category

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone} ({email}): {message}')
        return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product



# def home(request):
#     context_list = {'object_list': Product.objects.all()[:6]}
#
#     return render(request, 'catalog/home.html', context=context_list)
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'You have new message from {name} {phone} ({email}): {message}')
#     return render(request, 'catalog/contacts.html')
#
#
# def product_catalog(request):
#     context_list = {'object_list': Product.objects.all()}
#
#     return render(request, 'catalog/product_catalog.html', context=context_list)
#
#
# def product_info(request, pk):
#     category_item = {'object': Product.objects.get(pk=pk)}
#
#     return render(request, 'catalog/product_info.html', context=category_item)
