# Generated by Django 5.0.3 on 2024-11-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0020_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=2, unique=True),
        ),
    ]