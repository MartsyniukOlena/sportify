# Generated by Django 3.2.25 on 2024-05-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]