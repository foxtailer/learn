from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Rate, QuestionRate

#admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Rate)
admin.site.register(QuestionRate)


class ChoiceInline(admin.TabularInline): 
  model = Choice 
  extra = 3


class QuestionAdmin(admin.ModelAdmin): 
  fieldsets = [ (None, {"fields": ["question_text"]}), 
               ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}), ] 
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)