from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=1200)
    description = models.TextField(null=True, blank=True)
    # location = models.CharField(max_length=1200, blank=True, default="Pale Blue Dot")
    # job = models.CharField(max_length=1200, null=True, blank=True)

    def __str__(self):
        return self.name
