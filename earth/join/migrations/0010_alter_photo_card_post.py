# Generated by Django 5.0.3 on 2024-10-31 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0009_alter_photo_card_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='card_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decorated_images', to='join.cardpost'),
        ),
    ]