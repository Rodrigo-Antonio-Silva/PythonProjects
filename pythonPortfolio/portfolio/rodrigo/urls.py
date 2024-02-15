from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pessoal", views.pessoal, name="pessoal"),
    path("profissional", views.profissional, name='profissional')
]
