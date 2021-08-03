from django.shortcuts import render, HttpResponse

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