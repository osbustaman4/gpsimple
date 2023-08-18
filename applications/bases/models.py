from django.db import models

from applications.bases.managers import AppComandosMotorManager, GsObjectsManager, GsUserZonesManager, GsUsersManager


class T4562419803(models.Model):
    f1 = models.CharField(max_length=255, blank=True, null=True)
    f2 = models.CharField(max_length=255, blank=True, null=True)
    f3 = models.CharField(max_length=255, blank=True, null=True)
    f4 = models.CharField(max_length=255, blank=True, null=True)
    f5 = models.CharField(max_length=255, blank=True, null=True)
    f6 = models.CharField(max_length=255, blank=True, null=True)
    f7 = models.CharField(max_length=255, blank=True, null=True)
    f8 = models.CharField(max_length=255, blank=True, null=True)
    f9 = models.CharField(max_length=255, blank=True, null=True)
    f10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T4562419803'


class ApiAccess(models.Model):
    user = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    empresa = models.CharField(max_length=45)
    id_empresa = models.IntegerField(blank=True, null=True)
    tokenjwt = models.CharField(max_length=1024, blank=True, null=True)
    token_publico = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'API_Access'


class Ejecutasp(models.Model):
    uno = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EjecutaSP'


class IntegracionesUserObject(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.IntegerField()
    imei = models.CharField(max_length=100)
    patente = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Integraciones_user_object'


class Pruebacargamasiva(models.Model):
    primero = models.CharField(max_length=100, blank=True, null=True)
    segundo = models.CharField(max_length=100, blank=True, null=True)
    tercero = models.CharField(max_length=100, blank=True, null=True)
    cuarto = models.CharField(max_length=100, blank=True, null=True)
    quinto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PruebaCargaMasiva'


class AppAlertas(models.Model):
    imei = models.CharField(max_length=15)
    id_usuario = models.IntegerField()
    velocidad = models.IntegerField()
    sobre_limite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_alertas'


class AppComandosEnviados(models.Model):
    imei_dispositivo = models.CharField(max_length=100, blank=True, null=True)
    fecha_envio_comando = models.DateTimeField(blank=True, null=True)
    fecha_comando_aplicado = models.DateTimeField(blank=True, null=True)
    respuesta_gps = models.CharField(max_length=2048, blank=True, null=True)
    comando_enviado = models.CharField(max_length=100, blank=True, null=True)
    notificado = models.IntegerField(blank=True, null=True)
    comando_traduc = models.CharField(max_length=100, blank=True, null=True)
    id_comando = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'app_comandos_enviados'


class AppComandosHistorial(models.Model):
    patente = models.CharField(max_length=100)
    comando = models.CharField(max_length=100)
    ident_usuario = models.CharField(max_length=250)
    fecha = models.DateTimeField()
    empresa = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_comandos_historial'


class AppComandosMotor(models.Model):
    protocolo = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=20)
    comando = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    objects = AppComandosMotorManager()

    class Meta:
        managed = False
        db_table = 'app_comandos_motor'


class AppNotificaciones(models.Model):
    id_usuario = models.IntegerField()
    fecha_generada = models.DateTimeField()
    fecha_actualizada = models.DateTimeField()
    detalle = models.CharField(max_length=45)
    leida = models.IntegerField()
    oculta = models.IntegerField()
    tipo = models.CharField(max_length=15)
    imei_vehiculo = models.CharField(max_length=50, blank=True, null=True)
    identificador_tipo = models.IntegerField(blank=True, null=True)
    contador_reenvios = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_notificaciones'
        unique_together = (('id', 'id_usuario', 'fecha_generada'),)


class AppPandemiaTest(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    fecha = models.DateTimeField()
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app_pandemia_test'
        unique_together = (('usuario', 'fecha'),)


class AppPreguntasFrecuentes(models.Model):
    pregunta = models.CharField(max_length=1000, blank=True, null=True)
    detalle = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_preguntas_frecuentes'


class CodigosFallas(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigos_fallas'


class ComandosEnviados(models.Model):
    imei_dispositivo = models.CharField(max_length=100, blank=True, null=True)
    fecha_envio_comando = models.DateTimeField(blank=True, null=True)
    fecha_comando_aplicado = models.DateTimeField(blank=True, null=True)
    respuesta_gps = models.CharField(max_length=2048, blank=True, null=True)
    comando_enviado = models.CharField(max_length=100, blank=True, null=True)
    notificado = models.IntegerField(blank=True, null=True)
    comando_traduc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comandos_enviados'


class GsBillingPlans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    active = models.CharField(max_length=5)
    gbp_objects = models.IntegerField(db_column="objects")
    period = models.IntegerField()
    period_type = models.CharField(max_length=10)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gs_billing_plans'


class GsDevoluciones(models.Model):
    imei = models.CharField(max_length=45, blank=True, null=True)
    id_gps = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_devoluciones'


class GsDevolucionesCopy1(models.Model):
    imei = models.CharField(max_length=45, blank=True, null=True)
    id_gps = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_devoluciones_copy1'


class GsDtcData(models.Model):
    dtc_id = models.AutoField(primary_key=True)
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    imei = models.CharField(max_length=20)
    code = models.CharField(max_length=2000)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_dtc_data'


class GsGeocoderCache(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_geocoder_cache'


class GsMaps(models.Model):
    map_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    active = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    url = models.CharField(max_length=2048)
    layers = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_maps'


class GsObjectChat(models.Model):
    msg_id = models.AutoField(primary_key=True)
    dt_server = models.DateTimeField()
    imei = models.CharField(max_length=20)
    side = models.CharField(max_length=1)
    msg = models.CharField(max_length=2048)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gs_object_chat'


class GsObjectCmdExec(models.Model):
    cmd_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    dt_cmd = models.DateTimeField()
    imei = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gateway = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    cmd = models.CharField(max_length=256)
    status = models.IntegerField()
    re_hex = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_object_cmd_exec'


class GsObjectCustomFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    data_list = models.CharField(max_length=5)
    popup = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'gs_object_custom_fields'


class GsObjectData2(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overspeed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_2'


class GsObjectData321(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_321'


class GsObjectData352093083847912Copy1(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_352093083847912_copy1'


class GsObjectData354017113505131(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_354017113505131'


class GsObjectData356028083510025(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_356028083510025'


class GsObjectData356028083510099(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_356028083510099'


class GsObjectData359633102256372(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_359633102256372'


class GsObjectData4562419803(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_4562419803'


class GsObjectData65789024074843(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_65789024074843'


class GsObjectData67688031634680(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688031634680'


class GsObjectData67688031639887(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688031639887'


class GsObjectData67688031646387(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688031646387'


class GsObjectData67688031652708(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688031652708'


class GsObjectData67688031655000(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688031655000'


class GsObjectData67688032816237(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688032816237'


class GsObjectData67688032817672(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688032817672'


class GsObjectData67688032829511(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_67688032829511'


class GsObjectData7973777789(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_7973777789'


class GsObjectData860264053010451(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860264053010451'


class GsObjectData860264053012101(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860264053012101'


class GsObjectData860369050482734(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860369050482734'


class GsObjectData860896051039493(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860896051039493'


class GsObjectData860896051042216(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860896051042216'


class GsObjectData860896051042216Copy1(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860896051042216_copy1'


class GsObjectData86089605105596(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_86089605105596'


class GsObjectData860896051055960(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860896051055960'


class GsObjectData860896052378833(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_860896052378833'


class GsObjectData861585041279934(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_861585041279934'


class GsObjectData861585041282987(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_861585041282987'


class GsObjectData864292041792712(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864292041792712'


class GsObjectData864352041128869(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864352041128869'


class GsObjectData864352041145137(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864352041145137'


class GsObjectData864403041366403(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403041366403'


class GsObjectData864403041366668(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403041366668'


class GsObjectData864403041366684(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403041366684'


class GsObjectData864403042832916(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403042832916'


class GsObjectData864403042845017(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403042845017'


class GsObjectData864403042862889(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403042862889'


class GsObjectData864403042874579(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403042874579'


class GsObjectData864403042878802(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403042878802'


class GsObjectData864403044831700(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403044831700'


class GsObjectData864403044856004(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403044856004'


class GsObjectData864403045741346(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403045741346'


class GsObjectData864403045751535(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403045751535'


class GsObjectData864403045751535Copy1(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403045751535_copy1'


class GsObjectData864403045752087(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864403045752087'


class GsObjectData864606042358134(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864606042358134'


class GsObjectData864606042361328(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_864606042361328'


class GsObjectData867060037404320(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_867060037404320'


class GsObjectData867060037740079(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_867060037740079'


class GsObjectData867553055156277(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_867553055156277'


class GsObjectData868998039471319(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_868998039471319'


class GsObjectDataRsyp42(models.Model):
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    params = models.CharField(max_length=2048)
    overpass = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_object_data_RSYP42'


class GsObjectImg(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_file = models.CharField(max_length=50)
    imei = models.CharField(max_length=20)
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()
    altitude = models.FloatField()
    angle = models.FloatField()
    speed = models.FloatField()
    params = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'gs_object_img'


class GsObjectSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    param = models.CharField(max_length=20)
    data_list = models.CharField(max_length=5)
    popup = models.CharField(max_length=5)
    result_type = models.CharField(max_length=10)
    text_1 = models.CharField(max_length=50)
    text_0 = models.CharField(max_length=50)
    units = models.CharField(max_length=10)
    lv = models.FloatField()
    hv = models.FloatField()
    formula = models.CharField(max_length=50)
    calibration = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'gs_object_sensors'


class GsObjectServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    data_list = models.CharField(max_length=5)
    popup = models.CharField(max_length=5)
    odo = models.CharField(max_length=5)
    odo_interval = models.FloatField()
    odo_last = models.FloatField()
    engh = models.CharField(max_length=5)
    engh_interval = models.IntegerField()
    engh_last = models.IntegerField()
    days = models.CharField(max_length=5)
    days_interval = models.IntegerField()
    days_last = models.DateField()
    odo_left = models.CharField(max_length=5)
    odo_left_num = models.IntegerField()
    engh_left = models.CharField(max_length=5)
    engh_left_num = models.IntegerField()
    days_left = models.CharField(max_length=5)
    days_left_num = models.IntegerField()
    update_last = models.CharField(max_length=5)
    notify_service_expire = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'gs_object_services'


class GsObjects(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    protocol = models.CharField(max_length=50)
    net_protocol = models.CharField(max_length=3)
    ip = models.CharField(max_length=50)
    port = models.CharField(max_length=10)
    active = models.CharField(max_length=5)
    object_expire = models.CharField(max_length=5)
    object_expire_dt = models.DateField()
    manager_id = models.IntegerField()
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()
    altitude = models.FloatField()
    angle = models.FloatField()
    speed = models.FloatField()
    loc_valid = models.IntegerField()
    params = models.CharField(max_length=2048)
    dt_last_stop = models.DateTimeField()
    dt_last_idle = models.DateTimeField()
    dt_last_move = models.DateTimeField()
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=256)
    map_arrows = models.CharField(max_length=512)
    map_icon = models.CharField(max_length=5)
    tail_color = models.CharField(max_length=7)
    tail_points = models.IntegerField()
    device = models.CharField(max_length=30)
    sim_number = models.CharField(max_length=50)
    model = models.CharField(max_length=60)
    vin = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50)
    odometer_type = models.CharField(max_length=10)
    engine_hours_type = models.CharField(max_length=10)
    odometer = models.FloatField()
    engine_hours = models.IntegerField()
    fcr = models.CharField(max_length=512)
    time_adj = models.CharField(max_length=30)
    accuracy = models.CharField(max_length=1024)
    dt_chat = models.DateTimeField()
    overpass = models.IntegerField(blank=True, null=True)
    run_speed = models.IntegerField(blank=True, null=True)
    corte_motor = models.IntegerField(blank=True, null=True)
    comando_corte = models.CharField(max_length=30, blank=True, null=True)
    robado = models.IntegerField()
    satelites = models.IntegerField(blank=True, null=True)
    rele_activo = models.IntegerField()
    max_speed = models.IntegerField(blank=True, null=True)
    dt_robo = models.DateTimeField(blank=True, null=True)

    objects = GsObjectsManager()

    class Meta:
        managed = False
        db_table = 'gs_objects'
        unique_together = (('imei', 'robado'),)


class GsObjectsUnused(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    protocol = models.CharField(max_length=50)
    net_protocol = models.CharField(max_length=3)
    ip = models.CharField(max_length=50)
    port = models.CharField(max_length=10)
    dt_server = models.DateTimeField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gs_objects_unused'


class GsRilogbookData(models.Model):
    rilogbook_id = models.AutoField(primary_key=True)
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    imei = models.CharField(max_length=20)
    group = models.CharField(max_length=2)
    assign_id = models.CharField(max_length=30)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_rilogbook_data'


class GsSmsGatewayApp(models.Model):
    dt_sms = models.DateTimeField()
    identifier = models.CharField(max_length=20)
    number = models.CharField(max_length=50)
    message = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_sms_gateway_app'


class GsSystem(models.Model):
    key = models.CharField(max_length=32)
    value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_system'


class GsTemplates(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    subject = models.CharField(max_length=512)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_templates'


class GsThemes(models.Model):
    theme_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    active = models.CharField(max_length=5)
    theme = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'gs_themes'


class GsUserAccountRecover(models.Model):
    recover_id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dt_recover = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gs_user_account_recover'


class GsUserBillingPlans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    dt_purchase = models.DateTimeField()
    name = models.CharField(max_length=50)
    gubp_objects = models.IntegerField(db_column="objects")
    period = models.IntegerField()
    period_type = models.CharField(max_length=10)
    price = models.FloatField()
    flow_order = models.IntegerField(unique=True)
    payment_status = models.IntegerField()
    imei = models.ForeignKey(GsObjects, models.DO_NOTHING, db_column='imei')
    email = models.CharField(max_length=320, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_billing_plans'


class GsUserCmd(models.Model):
    cmd_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    gateway = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    cmd = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_user_cmd'


class GsUserCmdSchedule(models.Model):
    cmd_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    active = models.CharField(max_length=5)
    exact_time = models.CharField(max_length=5)
    exact_time_dt = models.DateTimeField()
    day_time = models.CharField(max_length=512)
    protocol = models.CharField(max_length=50)
    imei = models.TextField()
    gateway = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    cmd = models.CharField(max_length=256)
    dt_schedule_e = models.DateTimeField()
    dt_schedule_d = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gs_user_cmd_schedule'


class GsUserEvents(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    active = models.CharField(max_length=5)
    duration_from_last_event = models.CharField(max_length=5)
    duration_from_last_event_minutes = models.IntegerField()
    week_days = models.CharField(max_length=50)
    day_time = models.CharField(max_length=512)
    imei = models.TextField(blank=True, null=True)
    checked_value = models.CharField(max_length=1024)
    route_trigger = models.CharField(max_length=5)
    zone_trigger = models.CharField(max_length=5)
    routes = models.CharField(max_length=4096)
    zones = models.CharField(max_length=4096)
    notify_system = models.CharField(max_length=40)
    notify_email = models.CharField(max_length=5)
    notify_email_address = models.CharField(max_length=500)
    notify_sms = models.CharField(max_length=5)
    notify_sms_number = models.CharField(max_length=500)
    notify_arrow = models.CharField(max_length=5)
    notify_arrow_color = models.CharField(max_length=20)
    notify_ohc = models.CharField(max_length=5)
    notify_ohc_color = models.CharField(max_length=7)
    email_template_id = models.IntegerField()
    sms_template_id = models.IntegerField()
    cmd_send = models.CharField(max_length=5)
    cmd_gateway = models.CharField(max_length=5)
    cmd_type = models.CharField(max_length=5)
    cmd_string = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gs_user_events'


class GsUserEventsData(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=10)
    event_desc = models.CharField(max_length=512)
    notify_system = models.CharField(max_length=40)
    notify_arrow = models.CharField(max_length=5)
    notify_arrow_color = models.CharField(max_length=20)
    notify_ohc = models.CharField(max_length=5)
    notify_ohc_color = models.CharField(max_length=7)
    imei = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    dt_server = models.DateTimeField()
    dt_tracker = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()
    altitude = models.FloatField()
    angle = models.FloatField()
    speed = models.FloatField()
    params = models.CharField(max_length=2048)
    checked_value = models.IntegerField(blank=True, null=True)
    dt_event = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_events_data'


class GsUserEventsStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    dt_server = models.DateTimeField(blank=True, null=True)
    imei = models.CharField(max_length=20)
    event_status = models.IntegerField()
    notificado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gs_user_events_status'


class GsUserFailedLogins(models.Model):
    fail_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=100)
    dt_login = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gs_user_failed_logins'


class GsUserMarkers(models.Model):
    marker_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    marker_name = models.CharField(max_length=50)
    marker_desc = models.CharField(max_length=1024)
    marker_icon = models.CharField(max_length=256)
    marker_visible = models.CharField(max_length=5)
    marker_lat = models.FloatField()
    marker_lng = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gs_user_markers'


class GsUserObjectDrivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    driver_name = models.CharField(max_length=100)
    driver_assign_id = models.CharField(max_length=30)
    driver_idn = models.CharField(max_length=100)
    driver_address = models.CharField(max_length=200)
    driver_phone = models.CharField(max_length=50)
    driver_email = models.CharField(max_length=100)
    driver_desc = models.CharField(max_length=1024)
    driver_img_file = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'gs_user_object_drivers'


class GsUserObjectGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_name = models.CharField(max_length=50)
    group_desc = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_user_object_groups'


class GsUserObjectPassengers(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    passenger_name = models.CharField(max_length=100)
    passenger_assign_id = models.CharField(max_length=30)
    passenger_idn = models.CharField(max_length=100)
    passenger_address = models.CharField(max_length=200)
    passenger_phone = models.CharField(max_length=50)
    passenger_email = models.CharField(max_length=100)
    passenger_desc = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_user_object_passengers'


class GsUserObjectTrailers(models.Model):
    trailer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    trailer_name = models.CharField(max_length=100)
    trailer_assign_id = models.CharField(max_length=30)
    trailer_model = models.CharField(max_length=50)
    trailer_vin = models.CharField(max_length=50)
    trailer_plate_number = models.CharField(max_length=50)
    trailer_desc = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_user_object_trailers'


class GsUserObjects(models.Model):
    object_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    imei = models.CharField(max_length=20)
    group_id = models.IntegerField()
    driver_id = models.IntegerField()
    trailer_id = models.IntegerField()
    velocidad_alerta = models.IntegerField()
    alerta_enviada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_objects'


class GsUserPlacesGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_name = models.CharField(max_length=50)
    group_desc = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'gs_user_places_groups'


class GsUserReports(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    format = models.CharField(max_length=4)
    show_coordinates = models.CharField(max_length=5)
    show_addresses = models.CharField(max_length=5)
    zones_addresses = models.CharField(max_length=5)
    stop_duration = models.IntegerField()
    speed_limit = models.IntegerField()
    imei = models.TextField()
    zone_ids = models.TextField()
    sensor_names = models.TextField()
    data_items = models.TextField()
    schedule_period = models.CharField(max_length=10)
    schedule_email_address = models.CharField(max_length=1024)
    dt_schedule_d = models.DateTimeField()
    dt_schedule_w = models.DateTimeField()
    menor_a = models.IntegerField(blank=True, null=True)
    mayor_a = models.IntegerField(blank=True, null=True)
    dt_schedule_m = models.DateTimeField(blank=True, null=True)
    cantidad_r = models.IntegerField(blank=True, null=True)
    velocidad_superior_a = models.IntegerField(blank=True, null=True)
    velocidad_rutas = models.IntegerField(blank=True, null=True)
    diferencial_velocidad = models.IntegerField(blank=True, null=True)
    cantidad_horas = models.IntegerField(blank=True, null=True)
    fecha_envio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_reports'


class GsUserReportsGenerated(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    dt_report = models.DateTimeField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    format = models.CharField(max_length=4)
    gurg_objects = models.IntegerField(db_column="objects")
    zones = models.IntegerField()
    sensors = models.IntegerField()
    schedule = models.CharField(max_length=5)
    filename = models.CharField(max_length=100)
    report_file = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gs_user_reports_generated'


class GsUserRoutes(models.Model):
    route_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    route_name = models.CharField(max_length=50)
    route_color = models.CharField(max_length=7)
    route_visible = models.CharField(max_length=5)
    route_name_visible = models.CharField(max_length=5)
    route_deviation = models.CharField(max_length=5)
    route_points = models.CharField(max_length=21000)

    class Meta:
        managed = False
        db_table = 'gs_user_routes'


class GsUserTemplates(models.Model):
    template_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1024)
    subject = models.CharField(max_length=512)
    message = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'gs_user_templates'


class GsUserTokens(models.Model):
    id_usuario = models.IntegerField()
    token = models.CharField(unique=True, max_length=500)
    fecha = models.DateTimeField(blank=True, null=True)
    dispositivo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_tokens'


class GsUserUsage(models.Model):
    usage_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    dt_usage = models.DateField()
    login = models.IntegerField()
    email = models.IntegerField()
    sms = models.IntegerField()
    api = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gs_user_usage'


class GsUserZones(models.Model):
    zone_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    zone_name = models.CharField(max_length=1024)
    zone_color = models.CharField(max_length=7)
    zone_visible = models.CharField(max_length=5)
    zone_name_visible = models.CharField(max_length=5)
    zone_area = models.IntegerField()
    zone_vertices = models.TextField()
    imei = models.CharField(max_length=45, blank=True, null=True)
    plate_number = models.CharField(max_length=45, blank=True, null=True)
    contador_notificaciones = models.IntegerField(blank=True, null=True)
    identificador_activacion = models.IntegerField(blank=True, null=True)
    menor_igual_a = models.IntegerField(blank=True, null=True)
    mayor_igual_a = models.IntegerField(blank=True, null=True)

    objects = GsUserZonesManager()

    class Meta:
        managed = False
        db_table = 'gs_user_zones'


class GsUserZonesHistorial(models.Model):
    imei = models.CharField(max_length=45)
    geocerca = models.CharField(max_length=45)
    vehiculo = models.CharField(max_length=45)
    id_usuario = models.IntegerField()
    motivo = models.CharField(max_length=45, blank=True, null=True)
    leida = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gs_user_zones_historial'


class GsUsers(models.Model):
    active = models.CharField(max_length=5, db_collation='utf8_bin')
    account_expire = models.CharField(max_length=5, db_collation='utf8_bin')
    account_expire_dt = models.DateField()
    privileges = models.TextField(db_collation='utf8_bin')
    manager_id = models.IntegerField()
    manager_billing = models.CharField(max_length=5, db_collation='utf8_bin')
    username = models.CharField(max_length=100, db_collation='utf8_bin')
    password = models.CharField(max_length=100, db_collation='utf8_bin')
    sess_hash = models.CharField(max_length=100, db_collation='utf8_bin')
    email = models.CharField(max_length=100, db_collation='utf8_bin')
    api = models.CharField(max_length=5, db_collation='utf8_bin')
    api_key = models.CharField(max_length=100, db_collation='utf8_bin')
    dt_reg = models.DateTimeField()
    dt_login = models.DateTimeField()
    ip = models.CharField(max_length=100, db_collation='utf8_bin')
    notify_account_expire = models.CharField(max_length=5, db_collation='utf8_bin')
    notify_object_expire = models.CharField(max_length=5, db_collation='utf8_bin')
    info = models.CharField(max_length=1024, db_collation='utf8_bin')
    comment = models.CharField(max_length=2048, db_collation='utf8_bin')
    obj_add = models.CharField(max_length=5, db_collation='utf8_bin')
    obj_limit = models.CharField(max_length=5, db_collation='utf8_bin')
    obj_limit_num = models.IntegerField()
    obj_days = models.CharField(max_length=5, db_collation='utf8_bin')
    obj_days_dt = models.DateField()
    obj_edit = models.CharField(max_length=5, db_collation='utf8_bin')
    obj_history_clear = models.CharField(max_length=5, db_collation='utf8_bin')
    currency = models.CharField(max_length=3, db_collation='utf8_bin')
    timezone = models.CharField(max_length=30, db_collation='utf8_bin')
    dst = models.CharField(max_length=5, db_collation='utf8_bin')
    dst_start = models.CharField(max_length=20, db_collation='utf8_bin')
    dst_end = models.CharField(max_length=20, db_collation='utf8_bin')
    language = models.CharField(max_length=20, db_collation='utf8_bin')
    units = models.CharField(max_length=6, db_collation='utf8_bin')
    map_sp = models.CharField(max_length=7, db_collation='utf8_bin')
    map_is = models.FloatField()
    map_rc = models.CharField(max_length=7, db_collation='utf8_bin')
    map_rhc = models.CharField(max_length=7, db_collation='utf8_bin')
    groups_collapsed = models.CharField(max_length=100, db_collation='utf8_bin')
    od = models.CharField(max_length=10, db_collation='utf8_bin')
    ohc = models.CharField(max_length=256, db_collation='utf8_bin')
    chat_notify = models.CharField(max_length=40, db_collation='utf8_bin')
    sms_gateway_server = models.CharField(max_length=5, db_collation='utf8_bin')
    sms_gateway = models.CharField(max_length=5, db_collation='utf8_bin')
    sms_gateway_type = models.CharField(max_length=5, db_collation='utf8_bin')
    sms_gateway_url = models.CharField(max_length=2048, db_collation='utf8_bin')
    sms_gateway_identifier = models.CharField(max_length=20, db_collation='utf8_bin')
    places_markers = models.CharField(max_length=4, db_collation='utf8_bin')
    places_routes = models.CharField(max_length=4, db_collation='utf8_bin')
    places_zones = models.CharField(max_length=4, db_collation='utf8_bin')
    usage_email_daily = models.CharField(max_length=8, db_collation='utf8_bin')
    usage_sms_daily = models.CharField(max_length=8, db_collation='utf8_bin')
    usage_api_daily = models.CharField(max_length=8, db_collation='utf8_bin')
    usage_email_daily_cnt = models.IntegerField()
    usage_sms_daily_cnt = models.IntegerField()
    usage_api_daily_cnt = models.IntegerField()
    dt_usage_d = models.DateField()
    overpass = models.IntegerField()
    history_import = models.IntegerField(blank=True, null=True)
    rut = models.CharField(max_length=45, db_collation='utf8_bin', blank=True, null=True)
    sesion = models.IntegerField(blank=True, null=True)
    privilegios = models.CharField(max_length=255, db_collation='utf8_bin', blank=True, null=True)
    cartecf = models.IntegerField(db_column='cartecF', blank=True, null=True)  # Field name made lowercase.
    pass_verificada = models.IntegerField(blank=True, null=True)

    objects = GsUsersManager()

    class Meta:
        managed = False
        db_table = 'gs_users'


class HistorialInstaladores(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_instalador = models.BigIntegerField()
    imei = models.CharField(max_length=255)
    patente = models.CharField(max_length=255)
    km = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_instaladores'


class Instaladores(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.BigIntegerField()
    nombre = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rut = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instaladores'


class IntegracionesSinc(models.Model):
    sinc_id = models.AutoField(primary_key=True)
    sinc_integ = models.CharField(max_length=100, blank=True, null=True)
    sinc_imei = models.CharField(max_length=100, blank=True, null=True)
    sinc_dt_tracker = models.CharField(max_length=100, blank=True, null=True)
    sinc_dt_server = models.CharField(max_length=100, blank=True, null=True)
    sinc_params = models.CharField(max_length=100, blank=True, null=True)
    sinc_lat = models.FloatField(blank=True, null=True)
    sinc_lng = models.FloatField(blank=True, null=True)
    sinc_speed = models.FloatField(blank=True, null=True)
    sinc_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integraciones_sinc'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class RespuestaComando(models.Model):
    respuesta_comando = models.CharField(max_length=2048)
    fecha_comando = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta_comando'


class StBillingPlansObjects(models.Model):
    plan = models.OneToOneField(GsBillingPlans, models.DO_NOTHING, primary_key=True)
    imei = models.ForeignKey(GsObjects, models.DO_NOTHING, db_column='imei')

    class Meta:
        managed = False
        db_table = 'st_billing_plans_objects'
        unique_together = (('plan', 'imei'),)


class StCambiohora(models.Model):
    hora = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'st_cambiohora'


class StCodigosDtc(models.Model):
    tipo = models.CharField(primary_key=True, max_length=50, db_collation='utf8_general_ci')
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'st_codigos_dtc'
        unique_together = (('tipo', 'codigo', 'descripcion'),)


class StComportamientoconduccion(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    totalignicionno = models.IntegerField(db_column='totalIgnicionNo', blank=True, null=True)  # Field name made lowercase.
    totaltiempoconduccion = models.FloatField(db_column='totalTiempoConduccion', blank=True, null=True)  # Field name made lowercase.
    totaltiempodetenido = models.FloatField(db_column='totalTiempoDetenido', blank=True, null=True)  # Field name made lowercase.
    promediotiempoencendidocaliente = models.FloatField(db_column='promedioTiempoEncendidoCaliente', blank=True, null=True)  # Field name made lowercase.
    promediovelocidad = models.FloatField(db_column='promedioVelocidad', blank=True, null=True)  # Field name made lowercase.
    historialdevelocidadmasalta = models.FloatField(db_column='historialdeVelocidadMasAlta', blank=True, null=True)  # Field name made lowercase.
    historialmasaltarpm = models.FloatField(db_column='historialMasAltaRPM', blank=True, null=True)  # Field name made lowercase.
    totalaceleracionesbruscas = models.IntegerField(db_column='totalAceleracionesBruscas', blank=True, null=True)  # Field name made lowercase.
    totalfrenadasbruscas = models.IntegerField(db_column='totalFrenadasBruscas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'st_comportamientoconduccion'


class StHistorial(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    patente = models.CharField(max_length=50)
    vin = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    kms = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    usuariosat = models.CharField(db_column='usuarioSat', max_length=45, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_historial'
        unique_together = (('imei', 'patente', 'fecha', 'hora'),)


class StHistorialmasivo(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    fechainstalacion = models.DateField(db_column='fechaInstalacion')  # Field name made lowercase.
    fechacarga = models.DateField(db_column='fechaCarga')  # Field name made lowercase.
    horacarga = models.TimeField(db_column='horaCarga')  # Field name made lowercase.
    patente = models.CharField(max_length=50)
    vin = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    kms = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    usuariosat = models.CharField(db_column='usuarioSat', max_length=45, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_historialMasivo'
        unique_together = (('imei', 'patente', 'fechainstalacion', 'horacarga', 'fechacarga'),)


class StMaxSpeed(models.Model):
    ms_id = models.AutoField(primary_key=True)
    ms_start_latitude = models.CharField(max_length=100, blank=True, null=True)
    ms_start_longitude = models.CharField(max_length=100, blank=True, null=True)
    ms_end_latitude = models.CharField(max_length=100, blank=True, null=True)
    ms_end_longitude = models.CharField(max_length=100, blank=True, null=True)
    ms_speed = models.IntegerField(blank=True, null=True)
    ms_name_route = models.TextField(blank=True, null=True)
    ms_id_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_max_speed'


class StObjectExpiryNotif(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    notif_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'st_object_expiry_notif'


class StOtrosProveedores(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    patente = models.CharField(max_length=8)
    grupo = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=45, db_collation='utf8_slovak_ci')
    vacio1 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_otros_proveedores'


class StQrEstadoVehiculo(models.Model):
    patente = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pregunta = models.CharField(max_length=500, blank=True, null=True)
    respuesta = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_qr_estado_vehiculo'


class StQrPreguntas(models.Model):
    preguntas = models.CharField(max_length=300, blank=True, null=True)
    activado = models.IntegerField(blank=True, null=True)
    condicional = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_qr_preguntas'


class StQrUser(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'st_qr_user'


class StQrVehiculo(models.Model):
    rut = models.CharField(max_length=15)
    patente = models.CharField(max_length=10)
    fechayhora = models.DateTimeField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_qr_vehiculo'


class StSensors(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    group_sensor = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    param = models.CharField(max_length=20)
    data_list = models.CharField(max_length=5)
    popup = models.CharField(max_length=5)
    result_type = models.CharField(max_length=10)
    text_1 = models.CharField(max_length=50)
    text_0 = models.CharField(max_length=50)
    units = models.CharField(max_length=10)
    lv = models.FloatField()
    hv = models.FloatField()
    formula = models.CharField(max_length=50)
    calibration = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'st_sensors'


class StSensorsModels(models.Model):
    id_sensor_model = models.AutoField(primary_key=True)
    name_model = models.CharField(max_length=255)
    group_sensor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'st_sensors_models'


class StSms(models.Model):
    protocolo = models.CharField(max_length=45, blank=True, null=True)
    tipomensaje = models.CharField(db_column='tipoMensaje', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mensaje = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_sms'


class StTalleres(models.Model):
    empresa = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    comuna = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    sucursal = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_talleres'


class StUserProveedor(models.Model):
    user = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    empresa = models.CharField(max_length=45)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_grupo = models.IntegerField(blank=True, null=True)
    tokenjwt = models.CharField(max_length=1024, blank=True, null=True)
    token_publico = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'st_user_proveedor'


class StValidaEnvioDatos(models.Model):
    imei = models.IntegerField(unique=True)
    horayfecha = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'st_valida_envio_datos'


class Temporaltabla(models.Model):
    resultado = models.CharField(max_length=2000)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    imei = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporalTabla'


class TtDtc(models.Model):
    imei = models.CharField(max_length=20)
    dt_tracker = models.DateTimeField(blank=True, null=True)
    plate_number = models.CharField(max_length=50)
    model = models.CharField(max_length=60)
    code = models.CharField(max_length=2000)
    descripcion = models.CharField(max_length=700, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_dtc'


class TtJamming(models.Model):
    imei = models.CharField(max_length=20, blank=True, null=True)
    dt_server = models.DateTimeField(blank=True, null=True)
    dt_tracker = models.DateTimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    satelites = models.IntegerField(blank=True, null=True)
    params = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_jamming'


class TtTesting(models.Model):
    imei = models.CharField(max_length=20, blank=True, null=True)
    dato = models.CharField(max_length=10, blank=True, null=True)
    dt_servercon = models.DateTimeField(blank=True, null=True)
    dt_trackercon = models.DateTimeField(blank=True, null=True)
    latcon = models.FloatField(blank=True, null=True)
    lngcon = models.FloatField(blank=True, null=True)
    dt_serverfin = models.DateTimeField(blank=True, null=True)
    dt_trackerfin = models.DateTimeField(blank=True, null=True)
    latfin = models.FloatField(blank=True, null=True)
    lngfin = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_testing'


class TtValidaAppVehiculo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    plate_number = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    imei = models.CharField(max_length=20, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    corte_motor = models.IntegerField(blank=True, null=True)
    rele_activo = models.IntegerField(blank=True, null=True)
    robado = models.IntegerField(blank=True, null=True)
    alerta_velocidad = models.IntegerField(blank=True, null=True)
    comando_bd = models.IntegerField(blank=True, null=True)
    dt_tracker = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_valida_app_vehiculo'


class Usuarios(models.Model):
    usuario = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    rut = models.CharField(max_length=45, blank=True, null=True)
    privilegios = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vigilancia1S(models.Model):
    imei = models.CharField(primary_key=True, max_length=20)
    patente = models.CharField(max_length=50)
    robado = models.IntegerField()
    numero_telefono = models.CharField(max_length=20)
    sim_internacional = models.IntegerField(blank=True, null=True)
    comando = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vigilancia_1s'
        unique_together = (('imei', 'patente'),)
