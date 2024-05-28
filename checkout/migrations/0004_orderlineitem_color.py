# Generated by Django 3.2.25 on 2024-05-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_color_color_value'),
        ('checkout', '0003_auto_20240518_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.color'),
        ),
    ]
