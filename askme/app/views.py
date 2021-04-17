from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'tag': 'perl',
        'text': f'Some text for question #{idx}'
    } for idx in range(30)
]


def paginate(list, request):
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    list = paginator.get_page(page)
    return list


def index(request):
    content = paginate(questions, request)
    return render(request, 'index.html', {'questions': content})


def ask(request):
    return render(request, 'ask.html', {})


def login(request):
    return render(request, 'login.html', {})


def question(request, pk):
    question = questions[pk]
    return render(request, 'question.html', {"question": question, 'questions': questions})


def settings(request):
    return render(request, 'settings.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def tag(request, tag):
    content = paginate(questions, request)
    return render(request, 'tag.html', {"tag": tag, 'questions': content})


def hotquestions(request):
    content = paginate(questions, request)
    return render(request, 'hotquestions.html', {'questions': content})
