from django.db import models
from django.contrib.auth.models import User

class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # Middle name can be null
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    batch_year = models.IntegerField()
    contact_number = models.CharField(max_length=15)  # Adjust as necessary
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
