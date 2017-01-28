from django.db import models
from datetime import datetime


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    psk = models.CharField(max_length=128, unique=True)
    last_check_date = models.DateField(default=datetime.now())
