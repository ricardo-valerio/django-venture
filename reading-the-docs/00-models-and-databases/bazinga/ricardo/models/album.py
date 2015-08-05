from django.db import models
from .musician import Musician


class Album(models.Model):
    # ForeignKey, ManyToManyField and OneToOneField require the first argument
    #  to be a model class, so use the verbose_name keyword argument:
    artist = models.ForeignKey(Musician, verbose_name="album of the artist")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
