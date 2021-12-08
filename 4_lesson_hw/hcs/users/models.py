from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first_name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last_name')
    email = models.EmailField(blank=False, unique=True, verbose_name='email')
    date_of_birth = models.DateField(blank=True, default='2000-01-01', verbose_name='date_of_birth')
    # personal account for the housing and communal services
    personal_acc_hcs = models.FloatField(default=0.0, verbose_name='personal_acc_hcs')
    # personal account for the landline phone
    personal_acc_landline_phone = models.FloatField(default=0.0, verbose_name='personal_acc_landline_phone')
    # personal account for the long-distance phone
    personal_acc_distance_phone = models.FloatField(default=0.0, verbose_name='personal_acc_distance_phone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    flat_number = models.IntegerField(null=True, verbose_name='flat_number')
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, verbose_name='Address')

    # let it be so for now
    def get_absolute_url(self):
        return reverse_lazy('current_user', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-personal_acc_hcs']


class Address(models.Model):
    city_name = models.CharField(max_length=150, verbose_name='city_name')
    street = models.CharField(max_length=150, verbose_name='street')
    house = models.IntegerField(verbose_name='house')
    housing = models.IntegerField(null=True, verbose_name='housing')

    def __str__(self):
        return 'City: ' + str(self.city_name) + ', street: ' + str(self.street) + ', house: ' + str(self.house)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['city_name']


class Receipt(models.Model):
    amount_units = models.FloatField(verbose_name='amount_units')
    units = models.CharField(max_length=17, choices=(('m^2', 'square meters'), ('m^3', 'cubic meters'),
                                      ('Gcal', 'gigacalories'), ('minutes', 'minutes')), verbose_name='units')
    service = models.CharField(max_length=150, default='hot water', choices=(('hot water', 'hot water'),
                                                        ('cold water', 'cold water'),
                                                        ('heating', 'heating'),
                                                        ('landline phone', 'landline phone'),
                                                        ('long distance phone', 'long distance phone')),
                               verbose_name='service')
    amount_money = models.FloatField(verbose_name='amount_money')
    period_of_receipt = models.DateField(verbose_name='period_of_receipt')
    users = models.ForeignKey('Users', on_delete=models.CASCADE, null=True, verbose_name='users')

    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'
        ordering = ['period_of_receipt']