from django.http import Http404
from django.shortcuts import render, HttpResponse


ITEMS = (
    {'id': 1, 'name': 'Некий товар номер 1', 'quantity': 1},
    {'id': 2, 'name': 'Некий товар номер 2', 'quantity': 2},
    {'id': 3, 'name': 'Некий товар номер 3', 'quantity': 0},
    {'id': 4, 'name': 'Некий товар номер 4', 'quantity': 5},
    {'id': 5, 'name': 'Некий товар номер 5', 'quantity': 50},
)


# Create your views here.
def index(request):
    context = {
        'name': 'Михаил',
        'surname': 'Никитенко',
        'hobbies': ['web-programming', 'AVR-programming', 'HAM radio', 'YouTube']
    }
    return HttpResponse(render(request, 'index.html', context))


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
    return HttpResponse(render(request, 'MainApp/items.html', {'items': ITEMS}))


def item_details(request, pk):
    for item in ITEMS:
        if item['id'] == pk:
            return HttpResponse(render(request, 'MainApp/item_detail.html', {'item': item}))
    raise Http404
