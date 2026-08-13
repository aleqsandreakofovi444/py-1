from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Category, Product


class HomeView(ListView):
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category').order_by('price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (
            Category.objects.annotate(num_products=Count('products'))
            .filter(num_products__gt=0)
            .order_by('name')
        )
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object).order_by('price')
        return context


class SaleProductsView(ListView):
    template_name = 'shop/sale_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_sale=True).order_by('price')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Product'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Product'
        return context

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('shop:home')
