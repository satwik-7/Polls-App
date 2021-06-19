from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = "Polls Admin"
admin.site.index_title = "Welcome"
admin.site.site_title = "Polls Admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]    

admin.site.register(Question, QuestionAdmin)