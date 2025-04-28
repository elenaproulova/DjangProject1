from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Джанго</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница на Джанго</h1>")

def data(request):
    return HttpResponse("<p>Сегодня 28 апреля 2025 года и в Перми выпало очень много снега. Моя подруга оставила машину на работе и поехала домой с коллегой. А я не в Перми и снег выпадет у нас завтра. Придется тоже оставить машину дома, т.к. резину я уже поменяла. Но, может быть , повезет и все будет не так страшно.</p>")

def test(request):
    return HttpResponse("<h2>Просто текст на просто странице</h2>")