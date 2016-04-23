from __future__ import unicode_literals

from django.db import models

# Create your models here.





class PayableBills(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_description = models.CharField(max_length=200)