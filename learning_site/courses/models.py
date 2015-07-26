from django.db import models

# Create your models here.

class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	# field to be return when performing
	# Course.objects.all()
	def __str__(self):
		return self.title

# run migrations commands
# python3 manage.py makemigrations courses
# python3 manage.py migrate


class Step(models.Model):
	"""
		One-to-Many:
		- one course can have many steps
		- one step can have just one course
	"""
	title = models.CharField(max_length=255)
	description = models.TextField()
	order = models.IntegerField(default=0)
	course = models.ForeignKey(Course)

	def __str__(self):
		return self.title

# run migrations commands
# python3 manage.py makemigrations courses
# python3 manage.py migrate
