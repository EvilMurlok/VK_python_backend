from django.db import models


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

    def __str__(self):
        return self.name
