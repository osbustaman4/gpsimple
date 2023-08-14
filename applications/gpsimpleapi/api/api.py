from rest_framework.response import Response
from rest_framework import generics, status

from applications.bases.models import (
    AppNotificaciones
)
from applications.gpsimpleapi.api.serializer import AppNotificacionesSerializers

class AppNotificacionesUpdateView(generics.UpdateAPIView):

    queryset = AppNotificaciones.objects.all()
    serializer_class = AppNotificacionesSerializers
    
    def update(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        print(pk)
    

