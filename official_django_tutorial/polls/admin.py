from django.contrib import admin

# Register your models here.
#
from .models import Question, Choice

# Register the Question Model to appear on the admin site
# and have a out of the box form for fields.
#
# admin.site.register(Question)

"""
You’ll follow this pattern – create a model admin object, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for an object.
"""
# With TabularInline (instead of StackedInline), the related objects are displayed in a more compact, table-based format:
class ChoiceInline(admin.TabularInline):
    model = Choice
	# By default, provide enough fields for 3 choices.”
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# This particular change above makes the “Publication date” come
	# before the “Question” field:
	#
    # fields = ['pub_date', 'question_text']

    # By default, Django displays the str() of each object.
    # But sometimes it’d be more helpful if we could display individual fields. To
    # do that, use the list_display admin option, which is a tuple of field names
    # to display, as columns, on the change list page for the object:
    #
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # That adds a search box at the top of the change list. When somebody enters
    # search terms, Django will search the question_text field. You can use as
    # many fields as you’d like – although because it uses a LIKE query behind the
    # scenes, limiting the number of search fields to a reasonable number will
    # make it easier for your database to do the search.
    search_fields = ['question_text']
    # Now’s also a good time to note that change lists give you free pagination.
    # The default is to display 100 items per page.
    # Change list pagination, search boxes, filters, date-hierarchies, and
    # column-header-ordering all work together like you think they should.
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
	# This tells Django: “Choice objects are edited on the Question admin page.
	# Load the “Add question” page to see how that looks
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
