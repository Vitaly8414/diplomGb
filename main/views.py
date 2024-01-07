from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, Any] = {
    'title': 'Home',
    'content': 'Главная страница магазина - HOME'
}

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')


