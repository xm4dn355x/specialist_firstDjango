from django.http import Http404
from django.shortcuts import render, HttpResponse


ITEMS = (
    {'id': 1, 'name': 'Некий товар номер 1'},
    {'id': 2, 'name': 'Некий товар номер 2'},
    {'id': 3, 'name': 'Некий товар номер 3'},
    {'id': 4, 'name': 'Некий товар номер 4'},
    {'id': 5, 'name': 'Некий товар номер 5'},
)


# Create your views here.
def index(request):
    name = 'Никитенко М.В.'
    return HttpResponse(f'<h1>"Изучаем django"</h1><br><b>Автор</b>: <i>{name}</i>')


def about(request):
    name = 'Михаил'
    second_name = 'Викторович'
    surname = 'Никитенко'
    tel = '8-999-999-99-99'
    email = 'xm4dn355x@gmail.com'
    return HttpResponse(f'Имя: <b>{name}</b><br>Отчество: <b>{second_name}</b><br>'
                        f'Фамилия: <b>{surname}</b><br>Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')


def items(request):
    return HttpResponse('<br>'.join([f"""{i}: <a href="/item/{item['id']}">{item['name']}</a>"""
                                     for i, item in enumerate(ITEMS, start=1)]))


def item_details(request, pk):
    for item in ITEMS:
        if item['id'] == pk:
            return HttpResponse(f"""{item['name']}<br><a href="/items">Назад к списку товаров</a>""")
    # raise Http404   # По хорошему надо переопределять и использовать встроенный обработчик 404, но не сегодня,
    # мы даже шаблоны сегодня ещё не используем, всему своё время
    return HttpResponse(f'Товар с id:{pk} не найден<br><a href="/items">Назад к списку товаров</a>')
