from django.urls import path
from . import views

urlpatterns = [
    path('', views.scriptLauncher, name='scriptLauncher'),
    path('peticio-qr/', views.peticio_qr, name='peticio_qr'),
    path('processa-qr/', views.processa_qr, name='processa_qr'),
    path('formulari-maquinaria/', views.execute, name='execute'),
]
