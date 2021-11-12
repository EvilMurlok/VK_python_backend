from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    date_of_birth = models.DateField(blank=True, verbose_name='date_of_birth')
    # personal account for the housing and communal services
    personal_acc_hcs = models.FloatField(default=0.0, verbose_name='personal_acc_hcs')
    # personal account for the landline phone
    personal_acc_landline_phone = models.FloatField(default=0.0, verbose_name='personal_acc_landline_phone')
    # personal account for the long-distance phone
    personal_acc_distance_phone = models.FloatField(default=0.0, verbose_name='personal_acc_distance_phone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    # let it be so for now
    def get_absolute_url(self):
        return reverse('current_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-personal_acc_hcs']
