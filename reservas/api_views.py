from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reserva

@api_view(['GET'])
def reservas_hoy(request):
    from datetime import date
    hoy = date.today()

    reservas = Reserva.objects.filter(fecha=hoy)

    data = [
        {
            "usuario": r.usuario.nombre,
            "servicio": r.servicio.nombre,
            "hora": str(r.horario)
        }
        for r in reservas
    ]

    return Response(data)