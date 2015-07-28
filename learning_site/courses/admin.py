from django.contrib import admin

# Register your models here.

from .models import Course, Step


class StepInline(admin.StackedInline):
    '''
    Stacked Inline View for Step
    '''
    model = Step
    # min_num = 3
    # max_num = 20
    # extra = 1
    # raw_id_fields = (,)
admin.site.register(Step)


class CourseAdmin(admin.ModelAdmin):
    '''
        Admin View forCourse
    '''
    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        StepInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ['']
admin.site.register(Course, CourseAdmin)
