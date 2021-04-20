from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Question, Answer, LikeToQuestion, LikeToAnswer, Profile, Tag


def paginate(content_list, request):
    paginator = Paginator(content_list, 10)

    page = request.GET.get("page")
    content_list = paginator.get_page(page)
    return content_list


def index(request):
    questions = Question.objects.new()
    content = paginate(questions, request)
    return render(request, "index.html", {"content": content})


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def question(request, pk):
    _question = Question.objects.one_question(pk)
    answers = Answer.objects.filter(question=_question)
    content = paginate(answers, request)
    return render(request, "question.html", {"question": _question, "content": content})


def settings(request):
    return render(request, "settings.html", {})


def signup(request):
    return render(request, "signup.html", {})


def tag(request, tag_name):
    questions = Question.objects.all().filter(tags__name=tag_name)
    content = paginate(questions, request)
    return render(request, "tag.html", {"tag": tag_name, "content": content})


def hotquestions(request):
    questions = Question.objects.hot()
    content = paginate(questions, request)
    return render(request, "hotquestions.html", {"content": content})
