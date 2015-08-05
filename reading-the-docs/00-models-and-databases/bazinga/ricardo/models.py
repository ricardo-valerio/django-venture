from django.db import models

"""
https://docs.djangoproject.com/en/1.8/topics/db/models/

The name of the table, myapp_person, is automatically derived from some
model metadata but can be overridden. See Table names for more details.

An id field is added automatically, but this behavior can be overridden.
See Automatic primary key fields.

The CREATE TABLE SQL in this example is formatted using PostgreSQL syntax,
but it's worth  noting Django uses SQL tailored to the database backend
specified in your settings file.

Once you have defined your models, you need to tell Django you're going to
use those models. Do this by editing your settings file and changing the
INSTALLED_APPS  setting to add the name of the module that contains
your models.py.

FOR THIS REASON WE NEED TO CREATE AN APP IN ORDER TO HAVE MODELS

Be careful not to choose field names that conflict with the
models API like clean, save, or delete.

Django ships with dozens of built-in field types; you can find the complete
list in the model field reference. You can easily write your own fields
if Django's built-in ones don't do the trick; see Writing custom model fields.
"""
# BEFORE STEPS:
###############################################################################
# 0 |  python3 manage.py migrate
###############################################################################
# it creates the default django apps


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    SHIRT_SIZES = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
        )
    # The first element in each tuple is the value that will be stored in
    # the database, the second element will be displayed by the default form
    # widget or in a ModelChoiceField. Given an instance of a model object,
    # the display value for a choices field can be accessed using the
    # get_FOO_display method.
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    # Each field type, except: ForeignKey, ManyToManyField and OneToOneField,
    # takes an optional first positional argument – a verbose name.
    # If the verbose name isn’t given, Django will automatically create
    # it using the field’s attribute name, converting underscores to spaces.
    # The convention is not to capitalize the first letter of the verbose_name.
    # Django will automatically capitalize the first letter where it needs to.
    final_college_grade = models.IntegerField(
                            verbose_name="musician final college grade"
                          )


class Album(models.Model):
    # ForeignKey, ManyToManyField and OneToOneField require the first argument
    #  to be a model class, so use the verbose_name keyword argument:
    artist = models.ForeignKey(Musician, verbose_name="album of the artist")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


# AFTER STEPS:
###############################################################################
# 1 |  python3 manage.py makemigrations <app-name> --name <migration-file-name>
###############################################################################
#
#       python3 manage.py makemigrations ricardo --name andorinha
#       =========================================================
#
# it will create a folder:
#
# ricardo/migrations
# ├── 0001_andorinha.py
# ├── __init__.py
# └── __pycache__
#     ├── 0001_andorinha.cpython-34.pyc
#     └── __init__.cpython-34.pyc
#
###############################################################################
# 2 |  python3 manage.py sqlmigrate <app-name> <migration-file-name>
###############################################################################
#
#       python3 manage.py sqlmigrate ricardo 0001_andorinha
#       ===================================================
#
# it shows:
#
# BEGIN;
#     CREATE TABLE "ricardo_person" (
#           "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#           "first_name" varchar(30) NOT NULL,
#           "last_name" varchar(30) NOT NULL,
#           "address" varchar(40) NOT NULL);
# COMMIT;
#
###############################################################################
# 3 |  python3 manage.py migrate <app-name> <migration-file-name>
###############################################################################
#
#       python3 manage.py migrate ricardo 0001_andorinha
#       ================================================
#
#   Operations to perform:
#      Target specific migration: 0001_andorinha, from ricardo
#    Running migrations:
#      Rendering model states... DONE
#      Applying ricardo.0001_andorinha... OK
#
###############################################################################
# 4 |  python3 manage.py shell
###############################################################################
#
# In [1]: m = Musician(first_name="Ricardo",
#                      last_name="Valério",
#                      instrument="Piano",
#                      shirt_size="M")
#
# In [2]: m.save()
#
# In [3]: m.get_shirt_size_display()
# Out[3]: 'Medium'
#
# In [4]: a = Album(artist=m,
#                   name="e tudo o vento levou...",
#                   release_date="2016-12-12",
#                   num_stars=0)
#
# In [5]: a.save()
#
# In [25]: Musician.objects.all()
# Out[25]: [<Musician: Musician object>, <Musician: Musician object>]
#
# In [27]: Musician.objects.values()
# Out[27]: [
#   {  'shirt_size': 'M',
#      'last_name': 'Valério',
#      'instrument': 'Piano',
#      'first_name': 'Ricardo',
#      'id': 1
#   },
#   {  'shirt_size': 'L',
#      'last_name': 'Fonseca',
#      'instrument': 'Clarinete',
#      'first_name': 'Artur',
#      'id': 2
#   }
# ]
#
# In [28]: Musician.objects.values_list()
# Out[28]: [
#       (1, 'Ricardo', 'Valério', 'Piano', 'M'),
#       (2, 'Artur', 'Fonseca', 'Clarinete', 'L')
# ]
#
# In [29]: Musician.objects.values_list("first_name")
# Out[29]: [('Ricardo',), ('Artur',)]
#
# In [30]: Musician.objects.values_list("first_name", flat=True)
# Out[30]: ['Ricardo', 'Artur']
###############################################################################
# 5 |  Relationships
###############################################################################
#
# Many-to-one relationships
# =========================
#
# https://docs.djangoproject.com/en/1.8/topics/db/models/#many-to-one-relationships
#
# You can also create recursive relationships
# (an object with a many-to-one relationship to itself)
# and relationships to models not yet defined;
# see the model field reference for details.
#
# It’s suggested, but not required, that the name of a ForeignKey field
# be the name of the model, lowercase.
# You can, of course, call the field whatever you want. For example:
# I the above models we have "artist" instead of "musician"
#
# ForeignKey fields accept a number of extra arguments which are explained in
# the model field reference. These options help define how the relationship
# should work; all are optional.
#
# For details on accessing backwards-related objects, see the Following
# relationships backward example.
#
# For sample code, see the Many-to-one relationship model example.
#
#
# Many-to-many
# ============
#
# https://docs.djangoproject.com/en/1.8/topics/db/models/#many-to-many-relationships
#
# For example, if a Pizza has multiple Topping objects – that is, a Topping can
# be on multiple pizzas and each Pizza has multiple toppings
# – here’s how you’d represent that:
#
#
#    class Topping(models.Model):
#        # ...
#        pass
#

#    class Pizza(models.Model):
#        # ...
#        toppings = models.ManyToManyField(Topping)
#
#
# As with ForeignKey, you can also create recursive relationships
# (an object with a many-to-many relationship to itself) and relationships
# to models not yet defined; see the model field reference for details.
#
# It’s suggested, but not required, that the name of a ManyToManyField
# (toppings in the example above) be a plural describing the set of
# related model objects.
#
# It doesn’t matter which model has the ManyToManyField, but you should
# only put it in one of the models – not both.
#
# Generally, ManyToManyField instances should go in the object that’s going
# to be edited on a form. In the above example, toppings is in Pizza
# (rather than Topping having a pizzas ManyToManyField ) because it’s more
# natural to think about a pizza having toppings than a topping being on
# multiple pizzas. The way it’s set up above, the Pizza form would let users
# select the toppings.
#
# ManyToManyField fields also accept a number of extra arguments which are
# explained in the model field reference. These options help define how the
# relationship should work; all are optional.
#
# sometimes you may need to associate data with the relationship
# between two models.
#
# For example, consider the case of an application tracking the musical groups
# which musicians belong to. There is a many-to-many relationship between a
# person and the groups of which they are a member, so you could use a
# ManyToManyField to represent this relationship. However, there is a lot of
# detail about the membership that you might want to collect, such as the
# date at which the person joined the group.
#
# For these situations, Django allows you to specify the model that will
# be used to govern the many-to-many relationship. You can then put extra
# fields on the intermediate model. The intermediate model is associated with
# the ManyToManyField using the through argument to point to the model that
# will act as an intermediary. For our musician example, the code would
# look something like this:
#
#        class Person(models.Model):
#            name = models.CharField(max_length=128)
#
#            def __str__(self):
#                return self.name
#
#        class Group(models.Model):
#            name = models.CharField(max_length=128)
#            members = models.ManyToManyField(Person, through='Membership')
#
#            def __str__(self):
#                return self.name
#
#        class Membership(models.Model):
#            person = models.ForeignKey(Person)
#            group = models.ForeignKey(Group)
#            date_joined = models.DateField()
#            invite_reason = models.CharField(max_length=64)
#
