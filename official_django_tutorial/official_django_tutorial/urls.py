"""official_django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

"""
The tutorial project has just one app, polls. In real Django projects, there might be five,
ten, twenty apps or more. How does Django differentiate the URL names between them? For
example, the polls app has a detail view, and so might an app on the same project that is for
a blog. How does one make it so that Django knows which app view to create for a url when
using the {% url %} template tag?

The answer is to add namespaces to your root URLconf.
"""
urlpatterns = [
    url(r'^polls/', include("polls.urls", namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]

"""
The idea behind include() is to make it easy to plug-and-play URLs.
Since polls are in their own URLconf (polls/urls.py), they can be placed under
“/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root,
and the app will still work.
"""
