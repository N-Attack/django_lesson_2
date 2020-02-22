from django.db import models
from django.urls import reverse
from markdown import markdown
from django.contrib.auth.models import User


class Article(models.Model):
    header = models.CharField(max_length=128)
    markdown = models.TextField()
    pub_date = models.DateTimeField('date published')

    def save(self, **kwargs):
        self.html = markdown(self.markdown)
        super(Article, self).save()

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.article.pk})
