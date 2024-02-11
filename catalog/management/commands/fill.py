from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        list_categories = [
            {
                "title": "Clothes",
                "description": "Any clothes",
            },
            {
                "title": "Electronics",
                "description": "Any electronics",
            },
        ]
        list_products = [
            {
                "title": "Shirt",
                "description": "Shirt 2024",
                "product_image": "catalog/shirt.jpg",
                "id": 1,
                "purchase_price": 1000,
                "date_creation": "2024-01-01",
                "last_modified_date": "2023-01-01"
            },
            {
                "title": "Jeans",
                "description": "Jeans 2024",
                "product_image": "catalog/jeans.jpg",
                "id": 1,
                "purchase_price": 3000,
                "date_creation": "2024-01-01",
                "last_modified_date": "2023-01-01"
            },
            {
                "title": "Phone",
                "description": "Samsung Galaxy S24",
                "product_image": "catalog/S24.jpg",
                "id": 2,
                "purchase_price": 70000,
                "date_creation": "2024-01-01",
                "last_modified_date": "2024-01-01"
            },
            {
                "title": "Laptop",
                "description": "HP pavilion 2024",
                "product_image": "catalog/hp_pavilion.jpg",
                "id": 2,
                "purchase_price": 80000,
                "date_creation": "2024-01-01",
                "last_modified_date": "2024-01-01"
            },
            {
                "title": "Refrigerator",
                "description": "LG",
                "product_image": "catalog/LG_fridge.jpg",
                "id": 2,
                "purchase_price": 160000,
                "date_creation": "2024-01-01",
                "last_modified_date": "2024-01-01"
            }

        ]

        self.truncate_table_restart_id()

        for category in list_categories:
            Category.objects.create(**category)

        for product in list_products:
            Product.objects.create(**product)

        print('Данные добавлены')

    @classmethod
    def truncate_table_restart_id(cls):
        Product.objects.all().delete()
        print('Данные удалены')

