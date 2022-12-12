from django.db import models

# Create your models here.
class AdminUser(models.Model):
    username = models.CharField(
        primary_key = True, 
        max_length = 20, 
        unique = True
    )
    password = models.CharField(
        max_length = 20
    )