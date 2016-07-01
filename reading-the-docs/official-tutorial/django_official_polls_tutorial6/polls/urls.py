from django.conf.urls import url

from . import views

# namespacing urls specific to this app
# so it can be used for example as:
# {% url 'polls:detail' question.id %}
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# The DetailView generic view expects the primary key value captured
# from the URL to be called "pk", so we’ve changed question_id to pk
# for the generic views.
# Notice that ResultsView is also defined as as a
# Generic DetalView (see view.py)
