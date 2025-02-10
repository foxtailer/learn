from django.contrib import admin

from .models import Article, Rubric


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'rubric')
    search_fields = ('title', 'text')
    filter_by =('rubric')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric)
