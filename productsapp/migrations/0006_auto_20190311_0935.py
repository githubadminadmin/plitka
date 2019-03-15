# Generated by Django 2.1.5 on 2019-03-11 09:35

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0005_auto_20190307_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='productcategory', on_delete=django.db.models.deletion.CASCADE, to='productsapp.ProductСollection', verbose_name='Коллекция'),
        ),
        migrations.AlterField(
            model_name='product',
            name='copmositions',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collection', chained_model_field='collection', on_delete=django.db.models.deletion.CASCADE, to='productsapp.CompositionsCollection', verbose_name='Входит в состав'),
        ),
    ]