from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        "title": "Главная",
        "content": "Магазин Автотюнинга",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар.",
    }

    return render(request, "main/about.html", context)


def shipping(request):
    context = {
        "title": "Доставка",
        "content": "Информация о доставке",
        "text_on_page": "После оплаты доставка осуществляется в течении одного рабочего дня.",
    }

    return render(request, "main/shipping.html", context)


def contacts(request):
    context = {
        "title": "Контакты",
        "content": "Контактная информация:",
        "text_on_page": "Для связи вы можете обратиться по адресу пр.Мира 21 корпус 8.",
    }

    return render(request, "main/contacts.html", context)
