# Generated by Django 3.2.8 on 2021-11-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211109_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='views'),
        ),
    ]
