from django.contrib import admin
from .models import Usuario, Servicio, Horario, Reserva

admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(Horario)
admin.site.register(Reserva)
# Register your models here.
