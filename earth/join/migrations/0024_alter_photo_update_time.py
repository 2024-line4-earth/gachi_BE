# Generated by Django 5.1.2 on 2024-12-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0023_remove_frame_frame_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]