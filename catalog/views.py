from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.active_version = active_versions.last().name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        active_version = versions.filter(is_active=True).last()

        if active_version:
            product.active_version = active_version.name
        else:
            product.active_version = 'Нет активной версии'

        context_data['object'] = product
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:list_products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:list_products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:list_products')
