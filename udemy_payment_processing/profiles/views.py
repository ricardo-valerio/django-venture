from django.shortcuts import render
# from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello World!")
    return render(request, "home.html", {"subject": "World"})


def about(request):
    return render(request, "about.html", {})
