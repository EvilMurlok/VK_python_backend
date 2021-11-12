from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True)
    # personal account for the housing and communal services
    personal_acc_hcs = models.FloatField(default=0.0)
    # personal account for the landline phone
    personal_acc_landline_phone = models.FloatField(default=0.0)
    # personal account for the long-distance phone
    personal_acc_distance_phone = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    # let it be so for now
    def get_absolute_url(self):
        return reverse('current_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-personal_acc_hcs']
