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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceso/', views.acceso),
    path('menu/', views.menu),
    path('camara/', views.camara),
    path('leeAudio/', views.leeAudio),
    path('reconocerAudio/', views.reconocerAudio),
    path('reproduceAudio/', views.reproduceAudio),
    path('historiaView/', viewsClinico.nuevoView.as_view()),
    path('historia1View/', viewsClinico.historia1View),
    path('historiaExamenesView/', viewsClinico.historiaExamenesView),
    path('consecutivo_folios/', viewsClinico.consecutivo_folios),
    path('buscaExamenes/', viewsClinico.buscaExamenes),
    path('motivoSeñas/', viewsClinico.motivoSeñas),
    path('subjetivoSeñas/', viewsClinico.subjetivoSeñas),
    path('motivoInvidente/', viewsClinico.motivoInvidente),
    path('resMotivoInvidente/', viewsClinico.resMotivoInvidente),
    path('prueba/', viewsClinico.prueba),







]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)