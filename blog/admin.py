from django.contrib import admin

from blog.models import Article, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]


admin.site.register(Article, ArticleAdmin)
