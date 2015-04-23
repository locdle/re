from django.contrib import admin

# Register your models here.

from .models import Starq, Textq

class StarqAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question',            {'fields': ['starq_text']}),
        ('Star rating',         {'fields': ['rating']}),
    ]
    list_display = ('starq_text', 'rating', 'pub_date', 'is_rating_zero')
    list_filter = ['pub_date']
    search_fields = ['starq__text']

class TextqAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question',            {'fields': ['textq_text']}), 
        ('Answer',              {'fields': ['answer']}),
    ]
    list_display = ('textq_text', 'answer', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['textq__text']

admin.site.register(Starq, StarqAdmin)
admin.site.register(Textq, TextqAdmin)
