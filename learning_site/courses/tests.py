from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from .models import Course, Step

from django.core.urlresolvers import reverse

# to run tests:
# python3 manage.py test


###########################################################################
#    Tests for Models
###########################################################################


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title       = "Python Regular Expressions",
            description = "Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title       = "Python Testing",
            description = "Learn to write tests in Python"
        )

    def test_step_creation(self):
        step = Step.objects.create(
            title       = "Introduction to Doctests",
            description = "Learn to write tests in your docstrings.",
            course      = self.course
        )
        self.assertIn(step, self.course.step_set.all())


###########################################################################
#    Tests for Views
###########################################################################


class CourseViewsTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title       = "Python Testing",
            description = "Learn to write tests in python"
        )
        self.course2 = Course.objects.create(
            title       = "Python Ninja Course",
            description = "Learn python the Ninja Way"
        )
        self.step = Step.objects.create(
            title       = "Intro to Doctests",
            description = "Learn with docstrings",
            course      = self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse("courses:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context["courses"])
        self.assertIn(self.course2, resp.context["courses"])

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:course_detail',
                    kwargs={'course_pk': self.course.pk}
                ))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])

    def test_step_detail(self):
        resp = self.client.get(reverse('courses:step_detail',
                    kwargs={
                        'course_pk': self.course.pk,
                        'step_pk': self.step.pk
                    }
                ))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])
