# Generated by Django 2.2.7 on 2019-11-22 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
