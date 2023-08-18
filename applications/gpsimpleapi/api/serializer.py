from datetime import timezone
from rest_framework import serializers

from applications.bases.models import (
    AppNotificaciones,
    AppPreguntasFrecuentes, 
    GsUserObjects,
    GsUserZones,
    GsUsers
)


class AppNotificacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppNotificaciones
        fields = ('id_usuario',)

class AppNotificacionesNotiSelectSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppNotificaciones
        fields = ('__all__')

class GsUserObjectsSelializers(serializers.ModelSerializer):
    class Meta:
        model = GsUserObjects
        fields = ('__all__')

class GsUserZonesSelializers(serializers.ModelSerializer):
    class Meta:
        model = GsUserZones
        fields = ('user_id')

class GsUserZonesGeoDeleteSelializers(serializers.ModelSerializer):
    class Meta:
        model = GsUserZones
        fields = ('user_id', 'imei')

class AppPreguntasFrecuentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPreguntasFrecuentes
        fields = ('__all__')

class GsUsersSerializer(serializers.Serializer):
    id_usuario = serializers.IntegerField()

class InfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    company = serializers.CharField()
    address = serializers.CharField()
    post_code = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    phone1 = serializers.CharField()
    phone2 = serializers.CharField()

class GsUsersSerializerUpdate(serializers.Serializer):
    usuario = serializers.IntegerField()
    email = serializers.CharField()
    info = InfoSerializer()

class GsUsersSerializerLogin(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField()
    device = serializers.CharField()

class CarSelectSerializer(serializers.Serializer):
    name = serializers.CharField()
    plate_number = serializers.CharField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    alertas = serializers.IntegerField()
    imei = serializers.CharField()
    angle = serializers.FloatField()
    odometer = serializers.FloatField()
    active = serializers.CharField()
    comando_corte = serializers.BooleanField()
    protocol = serializers.CharField()
    ip = serializers.CharField()
    port = serializers.CharField()
    params = serializers.CharField()
    comandos = serializers.BooleanField()
    lastposi = serializers.DateTimeField()
    geocerca_imei = serializers.CharField()

class MotorCutSerializer(serializers.Serializer):
    imei = serializers.CharField()
    comando = serializers.CharField()

class GeoInsertSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    imei = serializers.CharField()
    vertices = serializers.CharField()
    patente = serializers.CharField()