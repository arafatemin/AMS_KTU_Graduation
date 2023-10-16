# Generated by Django 4.2.5 on 2023-10-08 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_stocks_productinstock_stocks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinstock',
            options={'ordering': ['-datetime'], 'verbose_name': 'ProductsInStock'},
        ),
        migrations.AlterModelOptions(
            name='stocks',
            options={'ordering': ['-name'], 'verbose_name': 'Stock'},
        ),
        migrations.RemoveField(
            model_name='productinstock',
            name='unit',
        ),
    ]
