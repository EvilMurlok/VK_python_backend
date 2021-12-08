# Generated by Django 3.2.8 on 2021-12-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='service',
            field=models.CharField(choices=[('hot water', 'hot water'), ('cold water', 'cold water'), ('heating', 'heating'), ('landline phone', 'landline phone'), ('long distance phone', 'long distance phone')], default='hot water', max_length=150, verbose_name='service'),
        ),
    ]
