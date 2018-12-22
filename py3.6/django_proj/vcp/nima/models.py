from django.db import models

# Create your models here.

class Accounts(models.Model):
    account_id = models.IntegerField(primary_key=True)
    account_name = models.CharField(max_length=255)
