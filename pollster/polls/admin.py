from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome To the Pollster Admin Area"

#This extends from TabularInLine
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #Qty of lines 


#This extends from ModelAdmin
class QuestionAdmin(admin.ModelAdmin):
    #This is an array with 
    fieldsets = [ (None, {'fields':['question_text']} ),
    ('Date Information', {'fields':['publish_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]


#admin.site.register(Question)
#admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
