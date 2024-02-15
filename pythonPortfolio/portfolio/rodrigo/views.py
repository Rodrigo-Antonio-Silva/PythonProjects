from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "rodrigo/index.html")


def pessoal(request):
    return HttpResponse("<h1>é isso pessoal</h1>")


def profissional(request):
    return HttpResponse("<h1>Profissional</h1>")
