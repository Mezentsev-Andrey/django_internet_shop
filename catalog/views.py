from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product_list(request):
    list_products = Product.objects.all()
    context_data = {
        'products': list_products
    }
    return render(request, 'catalog/index.html', context=context_data)


def product_info(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product_info.html', context=context)
