from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^$', views.course_list, name='course_list'),


    # UrlConfs for generic views
    url(r'^$', views.CourseListView.as_view(), name='index'),
]
