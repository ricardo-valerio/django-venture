from django.conf.urls import url

from . import views

# namespacing urls specific to this app
# so it can be used for example as:
# {% url 'polls:detail' question.id %}
# as seen in "polls/index.html" template
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
