# Generated by Django 5.1.3 on 2024-11-29 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0002_product_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_profile',
        ),
    ]
