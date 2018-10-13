# THIS FILE WAS CREATED...it didn't exist after running:
#  $  python manage.py startapp polls
######################################################
# Edited:

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

######################################################
