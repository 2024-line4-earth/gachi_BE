# Generated by Django 5.0.3 on 2024-11-03 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0015_delete_filtering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.cardpost'),
        ),
    ]
