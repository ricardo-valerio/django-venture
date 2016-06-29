from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# class QuestionAdmin(admin.ModelAdmin):
#     '''
#         Admin View for Question
#     '''
#     pass

# admin.site.register(Question, QuestionAdmin)


# class ChoiceAdmin(admin.ModelAdmin):
#     '''
#         Admin View for Choice
#     '''
#     pass

# admin.site.register(Choice, ChoiceAdmin)
