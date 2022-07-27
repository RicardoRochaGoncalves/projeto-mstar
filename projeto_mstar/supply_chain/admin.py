from django.contrib import admin
from .models import Mercadoria, Entrada, Saida, Local


admin.site.register(Mercadoria)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(Local)