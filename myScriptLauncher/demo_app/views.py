from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from demo_app.models import Lectura

def scriptLauncher(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def peticio_qr(request):
  template = loader.get_template('formulari.html')
  return HttpResponse(template.render())

def processa_qr(request):
  template = loader.get_template('formulari-qr.html')
  return HttpResponse(template.render())

def execute(request):
  # llegir els paràmetres que venen amb la URL
  ubicacio = request.GET.get('ubicacio', None)
  maquinaria = request.GET.get('maquinaria', None)
  
  #afegim les variables al context que passarem a la plantilla
  context = {
      'ubicacio': ubicacio,
      'maquinaria': maquinaria
  }
  return render(request, 'formulari.html', context)

def execute_bd(request):
  # llegir els paràmetres que venen amb la URL
  ubicacio = request.GET.get('ubicacio', None)
  maquinaria = request.GET.get('maquinaria', None)
  
  nueva_lectura = Lectura.objects.create(
        ubicacion=ubicacio,
        maquinaria=maquinaria
        # fecha_lectura is automatic
    )
  #afegim les variables al context que passarem a la plantilla
  context = {
      'ubicacio': ubicacio,
      'maquinaria': maquinaria
  }
  return render(request, 'feedback.html', context)
