# Generated by Django 3.2.25 on 2024-05-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_color',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
