from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница!!!',
        'values':['Some','Hello',123],
        'obj':{
            'car':'BMW',
            'age': 18,
            'hobby':'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return HttpResponse("""<h2> Наши контакты </h2>
    <p> Тел.: <b>8(495)123-33-64</b> </p>
    <p> Email.: <b>gjango@cool.com</b> </p>""")
