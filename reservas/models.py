from django.db import models
from django.core.exceptions import ValidationError
from datetime import time

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()

    def clean(self):
        if self.duracion_minutos <= 0:
            raise ValidationError("La duración debe ser mayor a 0")

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def clean(self):
        if self.hora_inicio >= self.hora_fin:
            raise ValidationError("La hora inicio debe ser menor a la hora fin")

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin}"


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha = models.DateField()

    def clean(self):
        existe = Reserva.objects.filter(
            horario=self.horario,
            fecha=self.fecha
        ).exclude(id=self.id).exists()

        if existe:
            raise ValidationError("Este horario ya está reservado")

    def __str__(self):
        return f"{self.usuario} - {self.fecha}"