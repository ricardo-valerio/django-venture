from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello World!")
    return render(request, "home.html", {"subject": "World"})


def about(request):
    return render(request, "about.html", {})


@login_required
def profile(request):
    user = request.user
    return render(request, "profile.html", {"user": user})
