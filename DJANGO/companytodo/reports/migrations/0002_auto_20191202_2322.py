# Generated by Django 2.2.7 on 2019-12-02 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
        ('areas', '0001_initial'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='production_line',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='areas.ProductionLine'),
            preserve_default=False,
        ),
    ]