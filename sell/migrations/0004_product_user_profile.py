# Generated by Django 5.1.3 on 2024-11-29 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_remove_product_user_profile'),
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='signin.userprofile'),
        ),
    ]