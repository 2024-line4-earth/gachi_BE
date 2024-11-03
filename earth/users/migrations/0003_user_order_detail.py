# Generated by Django 5.0.3 on 2024-11-03 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_purchase'),
        ('users', '0002_user_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='order_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.item'),
        ),
    ]
