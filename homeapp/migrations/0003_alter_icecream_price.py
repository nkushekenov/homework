# Generated by Django 4.2.5 on 2023-10-11 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_icecream_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]