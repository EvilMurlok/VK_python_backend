# Generated by Django 3.2.8 on 2021-12-06 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=150, verbose_name='city_name')),
                ('street', models.CharField(max_length=150, verbose_name='street')),
                ('house', models.IntegerField(verbose_name='house')),
                ('housing', models.IntegerField(null=True, verbose_name='housing')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'ordering': ['city_name'],
            },
        ),
        migrations.AddField(
            model_name='users',
            name='flat_number',
            field=models.IntegerField(null=True, verbose_name='flat_number'),
        ),
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address', verbose_name='Address'),
        ),
    ]