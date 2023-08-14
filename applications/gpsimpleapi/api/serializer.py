from rest_framework import serializers

from applications.bases.models import AppNotificaciones


class AppNotificacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppNotificaciones
        fields = ('__all__')