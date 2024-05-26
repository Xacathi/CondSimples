from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'page/model.html'


class Sobre(TemplateView):
    template_name = 'page/sobre.html'
