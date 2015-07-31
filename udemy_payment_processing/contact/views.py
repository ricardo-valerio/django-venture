from django.shortcuts import render

# Create your views here.

from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings


def index(request):
    form = ContactForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        print(form.cleaned_data["email"])
        subject = "Message from udemy django course"
        message = form.cleaned_data["comment"]
        mail_from_user = form.cleaned_data["email"]
        mail_to_user = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, mail_from_user,
                  mail_to_user,fail_silently=False)
        context = {"confirmed_message": "Thanks for your message!"}
    return render(request, "contact/index.html", context)
