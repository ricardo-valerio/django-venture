from django.shortcuts import render

# Create your views here.

######################################################
# Edited:

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World, We are at the poll's index view! :)")

######################################################
