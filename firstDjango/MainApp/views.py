from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    name = 'Никитенко М.В.'
    return HttpResponse(f'<h1>"Изучаем django"</h1><br><strong>Автор</strong>: <i>{name}</i>')

def about(request):
    name = 'Михаил'
    second_name = 'Викторович'
    surname = 'Никитенко'
    tel = '8-999-999-99-99'
    email = 'xm4dn355x@gmail.com'
    return HttpResponse(f'Имя: <strong>{name}</strong><br>Отчество: <strong>{second_name}</strong><br>'
                        f'Фамилия: <strong>{surname}</strong><br>Телефон: <strong>{tel}</strong><br>'
                        f'e-mail: <strong>{email}<strong>')