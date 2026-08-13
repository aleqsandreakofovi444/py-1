from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class ShopViewsTests(TestCase):
    def setUp(self):
        self.category_with_products = Category.objects.create(name='Electronics', slug='electronics')
        self.empty_category = Category.objects.create(name='Books', slug='books')
        Product.objects.create(name='Laptop', price=1200, is_sale=True, category=self.category_with_products)
        Product.objects.create(name='Mouse', price=25, is_sale=False, category=self.category_with_products)

    def test_home_page_shows_only_categories_with_products(self):
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(response.status_code, 200)
        categories = response.context['categories']
        self.assertEqual(list(categories), [self.category_with_products])
        self.assertEqual(categories[0].num_products, 2)

    def test_category_detail_page_shows_product_count(self):
        response = self.client.get(reverse('shop:category_detail', kwargs={'slug': self.category_with_products.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '2')
        self.assertContains(response, 'Laptop')
