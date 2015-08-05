# Fields

The most important part of a model – and the only required part of a model – is the list of database fields it defines. Fields are specified by class attributes. Be careful not to choose field names that conflict with the models API like clean, save, or delete.

Example:

    from django.db import models

    class Musician(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        instrument = models.CharField(max_length=100)

    class Album(models.Model):
        artist = models.ForeignKey(Musician)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()

Django uses the field class types to determine a few things:

* The database column type (e.g. INTEGER, VARCHAR).
* The default HTML widget to use when rendering a form field (e.g. <input type="text">, <select>).
* The minimal validation requirements, used in Django’s admin and in automatically-generated forms.

### Field types

    - AutoField
    - BigIntegerField
    - BinaryField
    - BooleanField
    - CharField
    - CommaSeparatedIntegerField
    - DateField
    - DateTimeField
    - DecimalField
    - DurationField
    - EmailField
    - FileField
         - FileField and FieldFile
    - FilePathField
    - FloatField
    - ImageField
    - IntegerField
    - IPAddressField
    - GenericIPAddressField
    - NullBooleanField
    - PositiveIntegerField
    - PositiveSmallIntegerField
    - SlugField
    - SmallIntegerField
    - TextField
    - TimeField
    - URLField
    - UUIDField
https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

### Field options

    - null
    - blank
    - choices
    - db_column
    - db_index
    - db_tablespace
    - default
    - editable
    - error_messages
    - help_text
    - primary_key
    - unique
    - unique_for_date
    - unique_for_month
    - unique_for_year
    - verbose_name
    - validators
https://docs.djangoproject.com/en/1.8/ref/models/fields/#common-model-field-options

### Relationship fields

    - ForeignKey (one to may)
    - ManyToManyField (many to many)
    - OneToOneField (one to one)

https://docs.djangoproject.com/en/1.8/topics/db/models/






