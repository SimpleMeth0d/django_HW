# Generated by Django 5.0.1 on 2024-02-11 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]
