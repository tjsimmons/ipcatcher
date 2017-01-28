from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True, blank=True)
    psk = models.CharField(max_length=128, unique=True)
    last_check_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.ip)
