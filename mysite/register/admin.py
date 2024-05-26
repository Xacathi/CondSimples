from django.contrib import admin

from .models import Administrador, Condominio, Apartamento, Proprietario, Morador

admin.site.register(Administrador)
admin.site.register(Condominio)
admin.site.register(Apartamento)
admin.site.register(Proprietario)
admin.site.register(Morador)