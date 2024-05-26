from django.urls import path
from .views import Home, Sobre


urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome_da_url'),
    path('', Home.as_view(), name='inicio'),
    path('sobre/', Sobre.as_view(), name='sobre'),
]