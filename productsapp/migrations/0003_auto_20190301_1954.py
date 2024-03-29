# Generated by Django 2.1.5 on 2019-03-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0002_auto_20190227_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Вес упаковки, кг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='col_in_upac',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Кол-во в упаковке'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Высота, см'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ширина, см'),
        ),
    ]
