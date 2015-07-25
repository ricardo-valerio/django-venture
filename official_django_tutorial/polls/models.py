from django.db import models

import datetime
from django.utils import timezone


# Create your models here.

# You can use an optional first positional argument to a Field to
# designate a human-readable name. That’s used in a couple of introspective
# parts of Django, and it doubles as documentation.
# If this field isn’t provided, Django will use the machine-readable name.
# In this example, we’ve only defined a human-readable name for
# Question.pub_date.
# For all other fields in this model, the field’s machine-readable name
# will suffice as its human-readable name.

# Some Field classes have required arguments.
# CharField, for example, requires that you give it a max_length.
# That’s used not only in the database schema, but in validation,
# as we’ll soon see.

# A Field can also have various optional arguments;
# in this case, we’ve set the default value of votes to 0.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# Note a relationship is defined, using ForeignKey.
# That tells Django each Choice is related to a single Question.
# And a Question can have many choices.

# Django supports all the common database relationships:
# many-to-one, many-to-many and one-to-one.

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# All this small bit of model code gives Django a lot of information.
# With it, Django is able to:
# Create a database schema (CREATE TABLE statements) for this app.
# Create a Python database-access API for accessing Question and Choice objects.

# But first we need to tell our project that the polls app is installed.
# Edit the mysite/settings.py file again, and change the INSTALLED_APPS
# setting to include the string 'polls'.

# Then Django Will know to include the polls app.
# Next let’s run another command:

####################################################################
# 	4- python3 manage.py makemigrations polls
####################################################################

# By running makemigrations, you’re telling Django that you’ve made some
# changes to your models (in this case, you’ve made new ones) and that you’d
# like the changes to be stored as a migration.

# Migrations are how Django stores changes to your models
# (and thus your database schema) - they’re just files on disk.
# You can read the migration for your new model if you like;
# it’s the file polls/migrations/0001_initial.py.
# Don’t worry, you’re not expected to read them every time Django makes one, but
# they’re designed to be human-editable in case you want to manually tweak
# how Django changes things.

# There’s a command that will run the migrations for you and
# manage your database schema automatically - that’s called migrate,
# and we’ll come to it in a moment - but first, let’s see what SQL
# that migration would run.
# The sqlmigrate command takes migration names and returns their SQL:


####################################################################
# 	5- python3 manage.py sqlmigrate polls 0001
####################################################################

# The sqlmigrate command doesn’t actually run the migration on your database
# - it just prints it to the screen so that you can see what SQL Django thinks
# is required. It’s useful for checking what Django is going to do or if you
# have database administrators who require SQL scripts for changes.

# If you’re interested, you can also run
#####################################################
# 	python3 manage.py check
#####################################################
#  this checks for any problems in your project without making
#  migrations or touching the database.


# Now, run migrate again to create those model tables in your database:

####################################################################
# 	6- python3 manage.py migrate
####################################################################

"""
The migrate command takes all the migrations that haven’t been applied
(Django tracks which ones are applied using a special table in your database
called django_migrations) and runs them against your database - essentially,
synchronizing the changes you made to your models with the schema
in the database.

Migrations are very powerful and let you change your models over time,
as you develop your project, without the need to delete your database or
tables and make new ones - it specializes in upgrading your database live,
without losing data. We’ll cover them in more depth in a
later part of the tutorial, but for now, remember the three-step
guide to making model changes:

    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.

The reason that there are separate commands to make and apply migrations
is because you’ll commit migrations to your version control system and ship
them with your app; they not only make your development easier, they’re also
useable by other developers and in production.
"""

# Now, let’s hop into the interactive Python shell and play around with
# the free API Django gives you. To invoke the Python shell, use this command:

####################################################################
# 	7- python3 manage.py shell
####################################################################


"""
>>> from polls.models import Question, Choice
# Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
[]

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
[<Question: Question object>]
"""

# Wait a minute. <Question: Question object> is, utterly,
# an unhelpful representation of this object.
# Let’s fix that by editing the Question model (in the polls/models.py file) and
# adding a __str__() method to both Question and Choice...
# Save the changes and start a new Python interactive shell by running
# python manage.py shell again.

##################################################################
# the first part of the tutorial finishes here, to see what's been
# addressed in part 2 go to the README.md file
##################################################################
