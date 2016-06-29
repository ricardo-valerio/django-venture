from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "blat/blat.html", {
        "my_name": "Ricardo",
    })
