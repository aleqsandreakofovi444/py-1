from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Category, Product


def home(request):
    categories = Category.objects.annotate(num_products=Count('products')).filter(num_products__gt=0).order_by('name')
    products = Product.objects.select_related('category').order_by('price')
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category).order_by('price')
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})


def sale_products(request):
    products = Product.objects.filter(is_sale=True).order_by('price')
    return render(request, 'shop/sale_products.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form, 'title': 'Add Product'})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form, 'title': 'Update Product'})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:home')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})
