# Generated by Django 2.1.5 on 2019-02-27 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tip',
        ),
        migrations.AlterField(
            model_name='compositionscollection',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.ProductType', verbose_name='Элемент коллекции'),
        ),
    ]
