from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    products = Product.objects.all().order_by('price')
    return render(request, 'store/home.html', {
        'categories': categories,
        'products': products,
    })


def category_detail(request, slug):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), slug=slug)
    products = category.products.all().order_by('price')
    return render(request, 'store/category_detail.html', {
        'categories': categories,
        'category': category,
        'products': products,
    })


def sales(request):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    products = Product.objects.filter(on_sale=True).order_by('price')
    return render(request, 'store/sales.html', {
        'categories': categories,
        'products': products,
    })


def about(request):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    return render(request, 'store/about.html', {
        'categories': categories,
    })
