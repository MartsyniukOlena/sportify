# Generated by Django 3.2.25 on 2024-05-26 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_product_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
