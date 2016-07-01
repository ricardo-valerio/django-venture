from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # We can use an optional first positional argument
    # to a Field to designate a human-readable name.
    pub_date = models.DateTimeField('date published')
    # For all other fields in this model, the field’s
    # machine-readable name will suffice as its human-readable name.

    # It’s important to add __str__() methods to your models,
    # not only for your own convenience when dealing with the interactive
    # prompt, but also because objects’ representations are used throughout
    # Django’s automatically-generated admin.
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
