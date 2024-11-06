# Generated by Django 5.0.3 on 2024-10-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0006_rename_frame_completed_frame_frame_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='join/')),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]