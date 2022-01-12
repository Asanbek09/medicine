from django.db import models


class Client(models.Model):
    date_of_birth = models.DateField(
        auto_now_add=False, null=True, blank=True)
    diagnoses = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
