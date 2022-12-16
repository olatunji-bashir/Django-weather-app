from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):  # show the actual city name on the dashboard
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Temperature(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'temperatures'
