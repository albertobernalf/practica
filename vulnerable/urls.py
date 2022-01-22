"""vulnerable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from camara import views
from django.conf  import settings
from django.conf.urls.static import  static
from clinico import views as viewsClinico
from mecanicosPacientes import views as viewsmecanicosPacientes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceso/', views.acceso),
    path('menu/', views.menu),
    path('menuAcceso/', views.menuAcceso),
    path('validaAcceso/', views.validaAcceso),
    path('menuAcceso/validaAcceso/', views.validaAcceso),
    path('contrasena/<str:documento>', views.contrasena),
    path('accesoEspecialidadMedico/<str:documento>', views.accesoEspecialidadMedico),
    path('grabar1/<str:username>,<str:contrasenaAnt>,<str:contrasenaNueva>,<str:contrasenaNueva2>', views.validaPassword),
    path('findOne/<str:username> , <str:password> /', views.Modal),


    path('salir/', views.salir),
    path('salir/validaAcceso/', views.validaAcceso),
    path('camara/', views.camara),
    path('leeAudio/', views.leeAudio),
    path('reconocerAudio/', views.reconocerAudio),
    path('reproduceAudio/', views.reproduceAudio),
    path('accesoEspecialidadMedico/historiaView/<str:documento>', viewsClinico.nuevoView.as_view()),

    path('historia1View/', viewsClinico.historia1View),
    path('historiaExamenesView/', viewsClinico.historiaExamenesView),
    path('consecutivo_folios/', viewsClinico.consecutivo_folios),
    path('buscaExamenes/', viewsClinico.buscaExamenes),
    path('motivoSeñas/', viewsClinico.motivoSeñas),
    path('subjetivoSeñas/', viewsClinico.subjetivoSeñas),
    path('motivoInvidente/', viewsClinico.motivoInvidente),
    path('resMotivoInvidente/', viewsClinico.resMotivoInvidente),
    path('prueba/', viewsClinico.prueba),
    path('manejoLuz/', viewsmecanicosPacientes.manejoLuz.as_view()),
    path('ambienteMusical/', viewsmecanicosPacientes.ambienteMusical.as_view()),

]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)