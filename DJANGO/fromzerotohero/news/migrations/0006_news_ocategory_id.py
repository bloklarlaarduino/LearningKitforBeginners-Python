# Generated by Django 2.2.6 on 2019-12-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20191215_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocategory_id',
            field=models.IntegerField(default=0),
        ),
    ]
