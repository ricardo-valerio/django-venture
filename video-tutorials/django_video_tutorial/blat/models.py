from django.db import models


class Blat(models.Model):
    """
    Description: Blat Model Description
    """
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)

    def total_likes(self):
        return self.like_set.count()

    # without this method inside the admin area
    # data would be presented in a non-human fashion
    def __str__(self):
        return self.text[:50]


class Like(models.Model):
    """
    Description: Like Model Description
    """
    blat = models.ForeignKey(Blat)
