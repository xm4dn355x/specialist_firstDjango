from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Item


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
    return HttpResponse(render(request, 'MainApp/items.html', {'items': Item.objects.all()}))


def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return HttpResponse(render(request, 'MainApp/item_detail.html', {'item': item}))
