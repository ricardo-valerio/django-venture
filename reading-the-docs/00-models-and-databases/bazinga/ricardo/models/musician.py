from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    is_cool = models.BooleanField(default=True)
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
