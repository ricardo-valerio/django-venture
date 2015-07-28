from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Course, Step
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


def course_detail(request, course_pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=course_pk)
    return render(request, "courses/course_detail.html", {"course": course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, "courses/step_detail.html", {"step": step})
