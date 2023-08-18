from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from applications.gpsimpleapi.api.api import (
    AppNotificacionesUpdateView, 
    AppNotificacionesNotiSelectRetrieveAPIView,
    CarHistoryAPIView,
    CarSelectApiView,
    GsUsersSerializerLoginApiView,
    MotorCutApiView,
    GeoInsertApiView,
    GsUserZonesApiView,
    GsUserZonesGeoDeleteApiView,
    AppPreguntasFrecuentesListAPIView,
    GsUsersSerializerApiView,
    GsUsersSerializerUpdateApiView
)

app_name = 'attendance_app'

urlpatterns = [

    path('car_history', CarHistoryAPIView.as_view(), name='car_history'),
    path('noti_select', AppNotificacionesNotiSelectRetrieveAPIView.as_view(), name='noti_select'),
    path('noti_read', AppNotificacionesUpdateView.as_view(), name='noti_read'),
    path('car_select', CarSelectApiView.as_view(), name='car_select'),
    path('motor_cut', MotorCutApiView.as_view(), name='motor_cut'),
    path('geo_insert', GeoInsertApiView.as_view(), name='geo_insert'),
    path('geo_select', GsUserZonesApiView.as_view(), name='geo_select'),
    path('geo_delete', GsUserZonesGeoDeleteApiView.as_view(), name='geo_delete'),
    path('question_select', AppPreguntasFrecuentesListAPIView.as_view(), name='question_select'),
    path('user_select', GsUsersSerializerApiView.as_view(), name='user_select'),
    path('user_update', GsUsersSerializerUpdateApiView.as_view(), name='user_update'),
    path('login_app', GsUsersSerializerLoginApiView.as_view(), name='login_app'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)