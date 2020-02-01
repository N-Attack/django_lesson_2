from django.http import HttpResponse
from django.template import loader
from .models import User

path = r"D:\Users\teacher\PycharmProjects\test_django\django_lesson\polls\templates\polls\index.html"


def index(request):
    template = loader.get_template("polls/index.html")
    context = {
        'items': User.objects.filter(name__startswith="r"),
    }
    return HttpResponse(template.render(context, request))

def users(request):
    template = loader.get_template("polls/users.html")
    context = {
        'users': User.objects.filter(name="rzerreer"),
    }
    return HttpResponse(template.render(context, request))

def work(request):
    text = request.GET.get("data")
    return HttpResponse(f"text is {text}")

