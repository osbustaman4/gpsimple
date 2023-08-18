import json
import traceback

from applications.bases.models import *

from applications.gpsimpleapi.api.serializer import (
    AppNotificacionesSerializers,
    AppNotificacionesNotiSelectSerializers,
    CarSelectSerializer,
    GsUserObjectsSelializers,
    GsUsersSerializerLogin,
    MotorCutSerializer,
    GeoInsertSerializer,
    GsUserZonesSelializers,
    GsUserZonesGeoDeleteSelializers,
    AppPreguntasFrecuentesSerializer,
    GsUsersSerializer,
    GsUsersSerializerUpdate
)

from django.apps import apps
from django.db import models
from django.db.models import (
    F,
    Q, 
    ExpressionWrapper, 
    DurationField, 
    Subquery, 
    OuterRef
)

from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from gpsimpledjango.Logger import Logger

from rest_framework.response import Response
from rest_framework import generics, status

class GsUsersSerializerLoginApiView(generics.CreateAPIView):
    serializer_class = GsUsersSerializerLogin

    @swagger_auto_schema(
        operation_id="user_select",
        operation_description="Obrener información del usuario",
        request_body=openapi.Schema(
            type='object',
            properties={
                'email': openapi.Schema(type='string'),
                'token': openapi.Schema(type='string'),
                'password': openapi.Schema(type='string'),
                'device': openapi.Schema(type='string'),
            },
            required=['email', 'token', 'password', 'device'],
        ),

        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "id": openapi.Schema(type="number"),
                        "email": openapi.Schema(type="string"),
                        "username": openapi.Schema(type="string"),
                        "tipo_user": openapi.Schema(type="string"),
                        "info": openapi.Schema(
                            type="object",
                            properties={
                                "name": openapi.Schema(type="number"),
                                "company": openapi.Schema(type="string"),
                                "address": openapi.Schema(type="string"),
                                "post_code": openapi.Schema(type="string"),
                                "city": openapi.Schema(type="string"),
                                "country": openapi.Schema(type="string"),
                                "phone1": openapi.Schema(type="string"),
                                "phone2": openapi.Schema(type="string"),
                                "email": openapi.Schema(type="string"),
                            },
                        ),
                        "timezone": openapi.Schema(type="string"),
                        "activo": openapi.Schema(type="string")
                    },
                )
            ),

            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        getAppComandosMotor = GsUsers.objects.login_app(serializer.initial_data)

        if "exito" in getAppComandosMotor:

            id_user = int(getAppComandosMotor.split(" ")[1])

            objectsGsUsers = GsUsers.objects.filter(id = id_user).values(
                'id', 
                'email', 
                'username', 
                'privileges', 
                'info', 
                'timezone', 
                'active' 
            )
            object = objectsGsUsers[0]
            response_to_page = {
                "id": object['id'],
                "email": object['email'],
                "username": object['username'],
                "tipo_user": json.loads(object['privileges'])['type'],
                "info": json.loads(object['info']),
                "timezone": object['timezone'],
                "activo": object['active']
            }
            return Response(response_to_page, status=status.HTTP_201_CREATED)

        else:
            response_to_page = {
                "message": "Not Found",
                "success": False
            }

            return Response(response_to_page, status=status.HTTP_404_NOT_FOUND) 


class GsUsersSerializerUpdateApiView(generics.CreateAPIView):

    serializer_class = GsUsersSerializerUpdate

    @swagger_auto_schema(
        operation_id="user_select",
        operation_description="Obrener información del usuario",
        request_body=openapi.Schema(
            type='object',
            properties={
                'usuario': openapi.Schema(type='integer', description='Identificador único del usuario'),
                "email": openapi.Schema(type="string"),
                "info": openapi.Schema(
                    type="object",
                    properties={
                        "address": openapi.Schema(type="string"),
                        "city": openapi.Schema(type="string"),
                        "company": openapi.Schema(type="string"),
                        "country": openapi.Schema(type="string"),
                        "name": openapi.Schema(type="string"),
                        "phone1": openapi.Schema(type="string"),
                        "phone2": openapi.Schema(type="string"),
                        "post_code": openapi.Schema(type="string"),
                    },
                )
            },
            required=['usuario', 'email', 'info'],
        ),

        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "id": openapi.Schema(type="number"),
                        "email": openapi.Schema(type="string"),
                        "info": openapi.Schema(
                            type="object",
                            properties={
                                "address": openapi.Schema(type="string"),
                                "city": openapi.Schema(type="string"),
                                "company": openapi.Schema(type="string"),
                                "country": openapi.Schema(type="string"),
                                "name": openapi.Schema(type="string"),
                                "phone1": openapi.Schema(type="string"),
                                "phone2": openapi.Schema(type="string"),
                                "post_code": openapi.Schema(type="string"),
                            },
                        ),
                    },
                )
            ),

            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        info = json.dumps(serializer.initial_data['info'])

        result = GsUsers.objects.filter(
            id=serializer.initial_data['usuario'],
            email=serializer.initial_data['email']
        ).update(
            info=info,
        )

        if result > 0:
            objectsGsUsers = GsUsers.objects.filter(id = serializer.initial_data['usuario']).values(
                'id', 
                'email', 
                'info', 
            )
            object = objectsGsUsers[0]
            response_to_page = {
                "id": object['id'],
                "email": object['email'],
                "info": json.loads(object['info']),
            }
            return Response(response_to_page, status=status.HTTP_201_CREATED)
        else:
            response_to_page = {
                "message": "Not Found",
                "success": False,
            }
            return Response(response_to_page, status=status.HTTP_404_NOT_FOUND)


class GsUsersSerializerApiView(generics.CreateAPIView):

    serializer_class = GsUsersSerializer

    @swagger_auto_schema(
        operation_id="user_select",
        operation_description="Obrener información del usuario",
        request_body=openapi.Schema(
            type='object',
            properties={
                'id_usuario': openapi.Schema(type='integer', description='Identificador único del usuario'),
            },
            required=['id_usuario'],
        ),

        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "id": openapi.Schema(type="number"),
                        "email": openapi.Schema(type="string"),
                        "username": openapi.Schema(type="string"),
                        "tipo_user": openapi.Schema(type="string"),
                        "info": openapi.Schema(
                            type="object",
                            properties={
                                "name": openapi.Schema(type="number"),
                                "company": openapi.Schema(type="string"),
                                "address": openapi.Schema(type="string"),
                                "post_code": openapi.Schema(type="string"),
                                "city": openapi.Schema(type="string"),
                                "country": openapi.Schema(type="string"),
                                "phone1": openapi.Schema(type="string"),
                                "phone2": openapi.Schema(type="string"),
                                "email": openapi.Schema(type="string"),
                            },
                        ),
                        "timezone": openapi.Schema(type="string"),
                        "activo": openapi.Schema(type="string")
                    },
                )
            ),

            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        objectsGsUsers = GsUsers.objects.filter(id = serializer.initial_data['id_usuario']).values(
            'id', 
            'email', 
            'username', 
            'privileges', 
            'info', 
            'timezone', 
            'active'
        )

        if not objectsGsUsers:
            response_to_page = {
                "mensaje": "No se encontro dato para mostrar",
                "success": False
            }
            return Response(response_to_page, status=status.HTTP_404_NOT_FOUND)
        else:

            object = objectsGsUsers[0]
            response_to_page = {
                "id": object['id'],
                "email": object['email'],
                "username": object['username'],
                "tipo_user": json.loads(object['privileges'])['type'],
                "info": json.loads(object['info']),
                "timezone": object['timezone'],
                "activo": object['active']
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED)


class AppPreguntasFrecuentesListAPIView(generics.ListAPIView):

    serializer_class = AppPreguntasFrecuentesSerializer
    queryset = AppPreguntasFrecuentes.objects.all()

    @swagger_auto_schema(
        operation_id="geo_delete",
        operation_description="desactivar geocercas en bases de datos",
        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "success": openapi.Schema(type="boolean"),
                        "detalle": openapi.Schema(
                            type="array",
                            items=openapi.Schema(
                                type="object",
                                properties={
                                    "id": openapi.Schema(type="number"),
                                    "pregunta": openapi.Schema(type="string"),
                                    "detalle": openapi.Schema(type="string"),
                                },
                            ),
                        ),
                    },
                )
            ),

            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not serializer.data:
            response_to_page = {
                "mensaje": "No hay preguntas frecuentes disponibles",
                "success": False
            }
            return Response(response_to_page, status=status.HTTP_404_NOT_FOUND)
        else:
            response_to_page = {
                "detalle": serializer.data,
                "mensaje": "Preguntas frecuentes obtenidas exitosamente",
                "success": True
            }
            return Response(response_to_page, status=status.HTTP_201_CREATED)


class GsUserZonesGeoDeleteApiView(generics.CreateAPIView):
    serializer_class = GsUserZonesGeoDeleteSelializers

    @swagger_auto_schema(
        operation_id="geo_delete",
        operation_description="desactivar geocercas en bases de datos",
        request_body=openapi.Schema(
            type='object',
            properties={
                'user_id': openapi.Schema(type='integer', description='Identificador único del usuario'),
                'imei': openapi.Schema(type='string', description='Imei del vehículo'),
            },
            required=['user_id'],
        ),
        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "success": openapi.Schema(type="boolean", description=True),
                    },
                )
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        result = GsUserZones.objects.filter(
            zone_name__startswith='Geocerca Temporal',
            zone_visible="true",
            zone_name_visible="true",
            imei=serializer.initial_data['imei'],
            user_id=serializer.initial_data['user_id']
        ).update(
            zone_visible="false",
            zone_name_visible="false",
            zone_color="#d50000"
        )

        if result > 0:
            response_to_page = {
                "mensaje": "Geocercas Eliminada",
                "success": True,
            }
            return Response(response_to_page, status=status.HTTP_201_CREATED)
        else:
            response_to_page = {
                "message": "Mot Found",
                "success": False,
            }
            return Response(response_to_page, status=status.HTTP_404_NOT_FOUND)


class GsUserZonesApiView(generics.CreateAPIView):
    serializer_class = GsUserZonesSelializers

    @swagger_auto_schema(
        operation_id="geo_select",
        operation_description="Obtener datos para dibujar los geocercas",
        request_body=openapi.Schema(
            type='object',
            properties={
                'user_id': openapi.Schema(type='integer', description='Identificador único del usuario'),
            },
            required=['user_id'],
        ),
        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "success": openapi.Schema(type="boolean"),
                        "detalle": openapi.Schema(
                            type="array",
                            items=openapi.Schema(
                                type="object",
                                properties={
                                    "imei": openapi.Schema(type="string"),
                                    "lat": openapi.Schema(type="number", format="float"),
                                    "lng": openapi.Schema(type="number", format="float"),
                                },
                            ),
                        ),
                    },
                )
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        query = GsUserZones.objects.filter(
            Q(zone_visible='true') &
            Q(zone_name_visible='true') &
            Q(zone_name__startswith='Geocerca Temporal') &
            Q(user_id=serializer.initial_data['user_id'])
        ).values('zone_vertices', 'imei')

        if not query:
            return Response(data={'message': f"404 not found", 'success': False}, status=status.HTTP_404_NOT_FOUND)

        results = query.all()

        transformed_results = []

        for result in results:
            zone_vertices = result['zone_vertices'].split(',')
            lat, lng = zone_vertices[0], zone_vertices[1]
            transformed_results.append({
                'imei': result['imei'],
                'lat': lat.strip(),
                'lng': lng.strip(),
            })

        response_to_page = {
            "mensaje": "Geocercas de Usuario",
            "success": True,
            "detalle": transformed_results
        }

        return Response(response_to_page, status=status.HTTP_201_CREATED)


class GeoInsertApiView(generics.CreateAPIView):

    serializer_class = GeoInsertSerializer

    @swagger_auto_schema(
        operation_id="geo_insert",
        operation_description="Activar geocercas en bases de datos",
        request_body=openapi.Schema(
            type='object',
            properties={
                'usuario': openapi.Schema(type='integer', description='Identificador único del usuario'),
                'imei': openapi.Schema(type='string', description='IMEI del vehículo'),
                'vertices': openapi.Schema(type='string', description='Latitud y longitud del vehículo'),
                'patent': openapi.Schema(type='string', description='Patente del vehículo'),
            },
            required=['usuario', 'imei', 'vertices', 'patent'],
        ),
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "detalle": openapi.Schema(type="string"),
                        "success": openapi.Schema(type="string"), 
                    },
                ),
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Error: 400 Bad Request",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo interpretar la solicitud dada una sintaxis inválida"),
                        "success": openapi.Schema(type="string", description="boolean false")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        getAppComandosMotor = GsUserZones.objects.geo_insert(serializer.initial_data)

        if getAppComandosMotor == "error":
            return Response(data={'message': f"404 not found", 'success': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            response_to_page = {
                "mensaje": f"Éxito para SP",
                "detalle": getAppComandosMotor,
                "success": True
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED) 


class MotorCutApiView(generics.CreateAPIView):

    serializer_class = MotorCutSerializer

    @swagger_auto_schema(
        operation_id="motor_cut",
        operation_description="Enviar comando de corte de motor y abrir/cerrar puertas",
        request_body=openapi.Schema(
            type='object',
            properties={
                'imei': openapi.Schema(type='string', description='IMEI del vehículo'),
                'comando': openapi.Schema(type='string', description='Comando para manipulación de un vehiculo, ejemplo motor, start o stop'),
            },
            required=['imei', 'comando'],
        ),
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "detalle": openapi.Schema(type="string"),
                        "success": openapi.Schema(type="string"), 
                    },
                ),
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado")
                    }
                )
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Error: 400 Bad Request",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo interpretar la solicitud dada una sintaxis inválida")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        getAppComandosMotor = AppComandosMotor.objects.motor_cut(serializer.initial_data)
        if getAppComandosMotor == "error":
            return Response(data={'message': f"{getAppComandosMotor} ya tiene comando agregado", 'success': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            response_to_page = {
                "mensaje": f"Éxito para SP",
                "detalle": getAppComandosMotor,
                "success": True
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED) 


class CarSelectApiView(generics.CreateAPIView):
    # Crear una instancia del serializador y pasarle los datos
    serializer_class = CarSelectSerializer

    @swagger_auto_schema(
        operation_id="car_select",
        operation_description="Obtener vehículos del usuario",
        request_body=openapi.Schema(
            type='object',
            properties={
                'id_usuario': openapi.Schema(type='integer', description='ID del usuario')
            },
            required=['id_usuario'],
        ),
        responses={
            201: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "dispos": openapi.Schema(
                            type="array",
                            items=openapi.Schema(
                                type="object",
                                properties={
                                    "name": openapi.Schema(type="string"),
                                    "plate_number": openapi.Schema(type="string"),
                                    "lat": openapi.Schema(type="number", format="float"),
                                    "lng": openapi.Schema(type="number", format="float"),
                                    "latLng": openapi.Schema(type="string"),
                                    "speed": openapi.Schema(type="number", format="float"),
                                    "imei": openapi.Schema(type="string"),
                                    "angle": openapi.Schema(type="number", format="float"),
                                    "odometer": openapi.Schema(type="number", format="float"),
                                    "active": openapi.Schema(type="string"),
                                    "comando_corte": openapi.Schema(type="string"),
                                    "protocol": openapi.Schema(type="string"),
                                    "ip": openapi.Schema(type="string"),
                                    "port": openapi.Schema(type="string"),
                                    "params": openapi.Schema(type="string"),
                                    "alertas": openapi.Schema(type="number", format="float"),
                                    "comandos": openapi.Schema(type="number", format="float"),
                                    "lastposi": openapi.Schema(type="string", format="date-time"),
                                    "geocerca_imei": openapi.Schema(type="string"),
                                },
                            ),
                        ),
                    },
                )
            ),

            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado")
                    }
                )
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Error: 400 Bad Request",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo interpretar la solicitud dada una sintaxis inválida")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        getGsObjects = GsObjects.objects.car_select(serializer.initial_data['id_usuario'])
        if getGsObjects:
            listDispos = []
            for object in getGsObjects:
                dataGsObj = {
                    "name": object[0],
                    "plate_number": object[1],
                    "lat": object[2],
                    "lng": object[3],
                    "latLng": object[4],
                    "speed": object[5],
                    "imei": object[6],
                    "angle": object[7],
                    "odometer": object[8],
                    "active": object[9],
                    "comando_corte": object[10],
                    "protocol": object[11],
                    "ip": object[12],
                    "port": object[13],
                    "params": object[14],
                    "alertas": object[15],
                    "comandos": object[16],
                    "lastposi": object[17],
                    "geocerca_imei": object[18]
                }
                listDispos.append(dataGsObj)

            response_to_page = {
                "mensaje": f"{ len(getGsObjects) } Vehículos Encontrados",
                "dispos": listDispos
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED)        
        return Response(data={'message': 'Error: 404 Not Found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class CarHistoryAPIView(generics.CreateAPIView):
    queryset = AppNotificaciones.objects.all()
    serializer_class = AppNotificacionesNotiSelectSerializers

    @swagger_auto_schema(
        operation_id="car_history",
        operation_description="Obtener historial de posiciones del vehículo por fecha",
        request_body=openapi.Schema(
            type='object',
            properties={
                'id_usuario': openapi.Schema(type='integer', description='ID del usuario'),
                'imei': openapi.Schema(type='string', description='IMEI del vehículo'),
                'fecha': openapi.Schema(type='string', description='YYYY-mm-dd', format="date"),
            },
            required=['id_usuario', 'imei', 'fecha'],
        ),
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "mensaje": openapi.Schema(type="string"),
                        "detalle": openapi.Schema(
                            type="array",
                            items=openapi.Schema(
                                type="object",
                                properties={
                                    "dt_tracker": openapi.Schema(type="string", format="date-time"),
                                    "lat": openapi.Schema(type="number", format="float"),
                                    "lng": openapi.Schema(type="number", format="float"),
                                    "altitude": openapi.Schema(type="number", format="float"),
                                    "speed": openapi.Schema(type="number", format="float"),
                                    "angle": openapi.Schema(type="number", format="float"),
                                    "params": openapi.Schema(type="string"),
                                },
                            ),
                        ),
                    },
                ),
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado")
                    }
                )
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Error: 400 Bad Request",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo interpretar la solicitud dada una sintaxis inválida")
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            getUserObjects = GsUserObjects.objects.filter(
                user_id=serializer.initial_data['id_usuario'], imei=serializer.initial_data['imei'])

            if not getUserObjects:
                return Response({"success": False, "message": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
            else:

                dataGsObjectData = self.get_data_by_imei(
                    serializer.initial_data['imei'])

                filtered_data = dataGsObjectData.objects.filter(
                    dt_tracker__startswith=serializer.initial_data['fecha']).order_by('dt_tracker')

                # Seleccionar los campos específicos
                filtered_data = filtered_data.values(
                    'dt_tracker', 'lat', 'lng', 'altitude', 'speed', 'angle', 'params'
                )

                response_to_page = {
                    "mensaje": f"historial para el día { serializer.initial_data['fecha'] }",
                    "detalle": filtered_data
                }

                return Response(response_to_page, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response(data={"error": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def get_data_by_imei(self, imei):
        # Obtén todas las clases de modelos definidas en la aplicación
        all_model_classes = apps.get_models()

        model_mapping = {}
        for model_class in all_model_classes:
            if model_class.__name__.startswith("GsObjectData"):
                imei_part = model_class.__name__[len("GsObjectData"):]
                model_mapping[imei_part] = model_class

        if imei in model_mapping:
            ModelClass = model_mapping[imei]
            try:
                return ModelClass
            except ModelClass.DoesNotExist:
                return Response(data={"error": "IMEI no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"error": "IMEI no válido"}, status=status.HTTP_400_BAD_REQUEST)


class AppNotificacionesNotiSelectRetrieveAPIView(generics.CreateAPIView):

    queryset = GsUserObjects.objects.all()
    serializer_class = GsUserObjectsSelializers

    @swagger_auto_schema(
        operation_id="noti_select",
        operation_description="Obtener notificaciones del usuario",
        request_body=openapi.Schema(
            type='object',
            properties={
                'id_usuario': openapi.Schema(type='integer', description='ID del usuario'),
                'fecha': openapi.Schema(type='string', description='YYYY-mm-dd', format="date"),
                'refrescar': openapi.Schema(type='boolean', description='Indica si se debe refrescar'),
            },
            required=['id_usuario', 'fecha', 'refrescar'],
        ),
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type="object",
                    properties={
                        "detalle": openapi.Schema(
                            type="array",
                            items=openapi.Schema(
                                type="object",
                                properties={
                                    "contador_reenvios": openapi.Schema(type="string"),
                                    "detalle": openapi.Schema(type="string"),
                                    "fecha_actualizada": openapi.Schema(type="string", format="date"),
                                    "fecha_generada": openapi.Schema(type="string", format="date"),
                                    "id": openapi.Schema(type="string"),
                                    "id_usuario": openapi.Schema(type="integer"),
                                    "identificador_tipo": openapi.Schema(type="string"),
                                    "imei_vehiculo": openapi.Schema(type="integer"),
                                    "leida": openapi.Schema(type="integer"),
                                    "oculta": openapi.Schema(type="string"),
                                    "tipo": openapi.Schema(type="string"),
                                },
                            ),
                        ),
                    }
                ),
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                        "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado")
                    }
                )
            ),
        },
    )
    def post(self, request, *args, **kwargs):

        try:
            serializer = self.serializer_class(data=request.data)
            user_id = serializer.initial_data['id_usuario']

            user_timezone_offset = Subquery(
                GsUsers.objects.filter(id=OuterRef('id_usuario')).annotate(
                    offset=ExpressionWrapper(
                        F('timezone') * -1,
                        output_field=DurationField()
                    )
                ).values('offset')[:1]
            )

            notifications = AppNotificaciones.objects.annotate(
                fecha_generada_with_offset=ExpressionWrapper(
                    F('fecha_generada') + user_timezone_offset,
                    output_field=models.DateTimeField()
                ),
                fecha_actualizada_with_offset=ExpressionWrapper(
                    F('fecha_actualizada') + user_timezone_offset,
                    output_field=models.DateTimeField()
                ),
            ).filter(id_usuario=user_id).order_by('-fecha_generada')[:15]

            notification_list = []
            for noti in notifications:
                notification_dict = {
                    "id_usuario": noti.id_usuario,
                    "fecha_generada": noti.fecha_generada,
                    "fecha_actualizada": noti.fecha_actualizada,
                    "detalle": noti.detalle,
                    "leida": noti.leida,
                    "oculta": noti.oculta,
                    "tipo": noti.tipo,
                    "imei_vehiculo": noti.imei_vehiculo,
                    "identificador_tipo": noti.identificador_tipo,
                    "contador_reenvios": noti.contador_reenvios,
                }

                notification_list.append(notification_dict)

            response_to_page = {
                "mensaje": "notificaciones",
                "detalle": notification_list
            }

            return Response(response_to_page, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response(data={"error": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class AppNotificacionesUpdateView(generics.CreateAPIView):
    serializer_class = AppNotificacionesSerializers
    queryset = AppNotificaciones.objects.all()

    @swagger_auto_schema(
        operation_id="noti_read",
        operation_description="Cambiar la notificación como leída",
        request_body=openapi.Schema(
            type='object',
            properties={
                'id_usuario': openapi.Schema(type='integer', description='ID del usuario.'),
            },
            required=['id_usuario'],
        ),
        responses={
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description="Error: 500 Internal Server Error",
                schema=openapi.Schema(
                    type='object',
                    properties={
                            "mensaje": openapi.Schema(type="string", description="Error: El servidor ha encontrado una situación que no sabe cómo manejarla")
                    }
                )
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Error: 404 Not Found",
                schema=openapi.Schema(
                    type='object',
                    properties={
                            "mensaje": openapi.Schema(type="string", description="Error: El servidor no pudo encontrar el contenido solicitado")
                    }
                )
            ),
            status.HTTP_200_OK: openapi.Response(
                description="Success: Ok",
                schema=openapi.Schema(
                    type='object',
                    properties={
                            "mensaje": openapi.Schema(type="string", description="Notificación actualizada")
                    }
                )
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                AppNotificaciones.objects.filter(id_usuario__in=[serializer.initial_data['id_usuario']]).update(
                    leida=1,
                    fecha_actualizada=timezone.now()
                )
                response_to_page = {
                    "mensaje": "Notificación actualizada"
                }
                return Response(response_to_page, status=status.HTTP_200_OK)
            else:
                Logger.add_to_log("error", str(serializer.errors))
                Logger.add_to_log("error", traceback.format_exc())
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            Logger.add_to_log("error", str(serializer.errors))
            Logger.add_to_log("error", traceback.format_exc())
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
