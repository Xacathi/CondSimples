from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, esse é meu primeiro site.")

from django.views.generic.edit import CreateView

from .models import Administrador, Condominio, Apartamento, Proprietario, Morador

from django.urls import reverse_lazy


