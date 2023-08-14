from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from applications.gpsimpleapi.api.api import AppNotificacionesUpdateView


app_name = 'attendance_app'

urlpatterns = [

    path('noti_select/', AppNotificacionesUpdateView.as_view(), name='noti_select'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)