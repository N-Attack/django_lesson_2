from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView

from blog.forms import CommentForm
from blog.models import Article, Comment


def index(request: HttpRequest):
    return HttpResponse('hello')


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-pub_date')[:5]


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ArticleView, self).get_context_data(**kwargs)
    #     context['form'] = CommentForm
    #     return context
    #


class NewComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment_form.html'

    def form_valid(self, form):
        # comment = form.save(commit=False)
        form.instance.article = get_object_or_404(Article, *self.args, **self.kwargs)
        return super(NewComment, self).form_valid(form)


def new_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article', pk=article.pk)
    else:
        form = CommentForm()

    return redirect('article', pk=article.pk)
