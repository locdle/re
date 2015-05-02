from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date',            {'fields':['pub_date']}),
        ('Rating',         {'fields':['rating']}),
        ('Response',   {'fields':['question_response']}),
    ]
    list_display = ('pub_date', 'rating', 'question_response')
    list_filter = ['rating']
admin.site.register(Question, QuestionAdmin)
