from django.shortcuts import render

# Create your views here.

from .models import Course
from django.http import HttpResponse
from django.views import generic


# def course_list(request):
# 	courses = Course.objects.all()
# 	return render(request, "courses/course_list.html", {"courses": courses})


# try generic views
class CourseListView(generic.ListView):
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()
