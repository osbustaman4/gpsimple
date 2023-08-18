from django.db import models, connection


class GsObjectsManager(models.Manager):

    def car_select(self, parameter):

        with connection.cursor() as cursor:
            cursor.execute(f""" 
                                SELECT 
                                    gs_objects.name, 
                                    gs_objects.plate_number, 
                                    gs_objects.lat, 
                                    gs_objects.lng, 
                                    CONCAT(
                                        gs_objects.lat, ', ', gs_objects.lng
                                    ) as latLng, 
                                    gs_objects.speed, 
                                    gs_objects.imei, 
                                    gs_objects.angle, 
                                    gs_objects.odometer, 
                                    gs_objects.active, 
                                    gs_objects.comando_corte, 
                                    gs_objects.protocol, 
                                    gs_objects.ip, 
                                    gs_objects.port, 
                                    gs_objects.params, 
                                    if(
                                        app_alertas.velocidad IS NULL, 0, app_alertas.velocidad
                                    ) as alertas, 
                                    if(
                                        gs_objects.comando_corte IS NULL 
                                        OR trim(gs_objects.comando_corte) = '', 
                                        false, 
                                        true
                                    ) as comandos, 
                                    if(
                                        gs_objects.dt_tracker < '2011-01-01 00:00:00' 
                                        OR gs_objects.dt_tracker IS NULL, 
                                        '1111-11-11 11:11:11', 
                                        gs_objects.dt_tracker
                                    ) as lastposi, 
                                    (
                                        SELECT 
                                        gs_user_zones.zone_vertices 
                                        FROM 
                                        gpsimple.gs_user_zones 
                                        WHERE 
                                        zone_visible = 'true' 
                                        AND zone_name_visible = 'true' 
                                        AND zone_name LIKE 'Geocerca Temporal%' 
                                        AND imei = gs_objects.imei 
                                        and gs_user_zones.user_id = gs_users.id
                                    ) as geocerca_imei 
                                    FROM 
                                        gs_objects 
                                        left JOIN gs_user_objects ON gs_objects.imei = gs_user_objects.imei 
                                        left JOIN gs_users ON gs_users.id = gs_user_objects.user_id 
                                        LEFT JOIN app_alertas ON app_alertas.imei = gs_objects.imei 
                                    where 
                                    gs_objects.active = 'true' 
                                    and gs_users.id = { parameter }
                                """)
            results = cursor.fetchall()
        return results
    

class AppComandosMotorManager(models.Manager):
    
    def motor_cut(self, parameter):
        with connection.cursor() as cursor:
            cursor.execute("CALL appv2_vehiculos_corte_motor(%s, %s)", (parameter['imei'], parameter['comando']))
            return cursor._rows[0][0]
        

class GsUserZonesManager(models.Manager):

    def geo_insert(self, parameter):
        with connection.cursor() as cursor:
            cursor.execute("CALL appv2_geocercas_insertar(%s, %s, %s, %s)", (parameter['usuario'], parameter['imei'], parameter['vertices'], parameter['patent']))
            return cursor._rows[0][0]
        

class GsUsersManager(models.Manager):

    def login_app(self, parameter):
        with connection.cursor() as cursor:
            cursor.execute("CALL wsapp_login(%s, %s, %s, %s)", (parameter['email'], parameter['password'], parameter['token'], parameter['device']))
            return cursor._rows[0][0]