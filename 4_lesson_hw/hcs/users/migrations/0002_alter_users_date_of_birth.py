# Generated by Django 3.2.8 on 2021-11-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-01-01', verbose_name='date_of_birth'),
        ),
    ]
