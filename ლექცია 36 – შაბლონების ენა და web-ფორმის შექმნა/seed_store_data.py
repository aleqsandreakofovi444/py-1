import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
import django

django.setup()

from store.models import Category, Product

CATEGORY_DATA = [
    {'name': 'Electronics', 'slug': 'electronics'},
    {'name': 'Books', 'slug': 'books'},
    {'name': 'Home & Kitchen', 'slug': 'home-kitchen'},
    {'name': 'Toys', 'slug': 'toys'},
]

PRODUCT_DATA = [
    {
        'name': 'Wireless Headphones',
        'description': 'Noise-cancelling over-ear headphones with long battery life.',
        'price': 99.99,
        'discounted_price': 79.99,
        'category_slug': 'electronics',
    },
    {
        'name': 'Smartphone Stand',
        'description': 'Adjustable desk stand for mobiles and tablets.',
        'price': 19.99,
        'discounted_price': None,
        'category_slug': 'electronics',
    },
    {
        'name': 'Cooking Recipe Book',
        'description': 'Delicious recipes for everyday meals.',
        'price': 24.50,
        'discounted_price': 19.99,
        'category_slug': 'books',
    },
    {
        'name': 'Science Fiction Novel',
        'description': 'A thrilling journey through space and time.',
        'price': 15.00,
        'discounted_price': None,
        'category_slug': 'books',
    },
    {
        'name': 'Ceramic Coffee Mug',
        'description': 'Durable mug with a modern matte finish.',
        'price': 12.00,
        'discounted_price': 9.50,
        'category_slug': 'home-kitchen',
    },
    {
        'name': 'Kitchen Knife Set',
        'description': 'Stainless steel chef knives for daily use.',
        'price': 49.99,
        'discounted_price': None,
        'category_slug': 'home-kitchen',
    },
    {
        'name': 'Building Blocks Set',
        'description': 'Creative construction toy for kids age 5+.',
        'price': 29.99,
        'discounted_price': 24.99,
        'category_slug': 'toys',
    },
    {
        'name': 'Puzzle Board Game',
        'description': 'Family-friendly logic puzzle game.',
        'price': 22.00,
        'discounted_price': None,
        'category_slug': 'toys',
    },
]


def run():
    Category.objects.all().delete()
    Product.objects.all().delete()

    categories = {}
    for item in CATEGORY_DATA:
        category = Category.objects.create(name=item['name'], slug=item['slug'])
        categories[item['slug']] = category

    for item in PRODUCT_DATA:
        Product.objects.create(
            category=categories[item['category_slug']],
            name=item['name'],
            description=item['description'],
            price=item['price'],
            discounted_price=item['discounted_price'],
        )

    print('Seed data created successfully.')


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
    run()
