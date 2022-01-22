from django.shortcuts import render

# Create your views here.

import numpy as np
import cv2
import uuid
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import os
import speech_recognition as sr
import time
import json
import pyttsx3
import MySQLdb



def camara(request):
    print("Entre Camara")
    cap= cv2.VideoCapture(0)

  #  while(True):
    ret , frame = cap.read()

    if ret:
            archivo=request.GET["nombre"]
            nombre_foto = archivo + ".jpg"
            cv2.imshow('Visor Familia Camacho', frame)
         #   cv2.imwrite( nombre_foto, frame)
            path = 'c:/EntornosPython/vulne/vulnerable/usuarios/static/usuarios'
            cv2.imwrite(os.path.join(path, nombre_foto), frame)
            datos = {"nombre": nombre_foto, "mensaje": " Fotografia tomada correctamente "}

            print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
    else:
        datos = {"nombre": nombre_foto, "mensaje": "Error al acceder a la cámara"}
        print("Error al acceder a la cámara")



 #       if cv2.waitKey(1) & 0xFF == ord('q'):
 #           break
    print("chao")
    cap.release()
    cv2.destroyAllWindows()

    return HttpResponse(json.dumps(datos))

def menu(request):
    print("Ingreso a menu")
    return render(request, "home1.html")


def acceso(request):
    print("Ingreso a acceso")
    return render(request, "home.html")

def menuAcceso(request):
    print("Ingreso a acceso")

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM planta_tiposPlanta"
    cur.execute(comando)
    print(comando)

    perfiles = []
    context = {}

    for id, nombre in cur.fetchall():
        perfiles.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(perfiles)

    context['Perfiles'] = perfiles

    return render(request, "accesoPrincipal.html", context)




def accesoEspecialidadMedico(request, documento):
    print("Ingreso a acceso")
    print ("el medico es")
    print (documento)


    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur = miConexion.cursor()
    comando = "select e.id id ,e.nombre nombre from clinico_especialidadesmedicos c, clinico_especialidades e , planta_planta p where p.documento = '" + documento + "' AND c.id_medico_id=p.id and c.id_especialidad_id=e.id"
    cur.execute(comando)
    print(comando)

    perfiles = []
    context = {}

    for id, nombre in cur.fetchall():
        perfiles.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(perfiles)

    context['Perfiles'] = perfiles
    context['documento'] = documento

    return render(request, "accesoEspecialidadMedico.html", context)

def Modal(request, username, password):

        print("Entre a Modal")
        print(username)
        print(password)

        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
        cur1 = miConexion1.cursor()
        comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "'"
        print(comando)
        cur1.execute(comando)

        UsuariosHc = {}

        for documento, contrasena in cur1.fetchall():
            UsuariosHc = {'username': documento, 'contrasena': contrasena}

        miConexion1.close()
        print(UsuariosHc)
        return JsonResponse(UsuariosHc, safe=False)
        # return HttpResponse(UsuariosHc)


def validaPassword(request, username, contrasenaAnt,contrasenaNueva,contrasenaNueva2):
    print("Entre ValidaPassword" )
    username = request.POST["username"]
    contrasenaAnt = request.POST["contrasenaAnt"]
    contrasenaNueva = request.POST["contrasenaNueva"]
    contrasenaNueva2 = request.POST["contrasenaNueva2"]

    print(username)
    print(contrasenaAnt)
    print(contrasenaNueva)
    print(contrasenaNueva2)

    miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur1 = miConexion1.cursor()
    comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "'"
    print(comando)
    cur1.execute(comando)

    UsuariosHc = []
    context = {}

    for documento, contrasena in cur1.fetchall():
        UsuariosHc = {'username': documento, 'contrasena': contrasena}

    miConexion1.close()
    print(UsuariosHc)

    if UsuariosHc == []:


        context['Error'] = "Personal invalido ! "
        print(context)


        return JsonResponse(context, safe=False)
        #return render(request, "accesoPrincipal.html", context)

    else:
        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
        cur1 = miConexion1.cursor()
        comando = "UPDATE planta_planta SET contrasena = '" +  str(contrasenaNueva) + "' WHERE documento = '" + str(username) + "'"
        print(comando)
        cur1.execute(comando)
        miConexion1.commit()
        miConexion1.close()
        context['Error'] = "Contraseña Actualizada ! "
        print(context)
        return JsonResponse(context, safe=False)
        #return render(request, "accesoPrincipal.html", context)


    #return JsonResponse(UsuariosHc, safe=False)




def contrasena(request, documento):

    print("Entre cambio contrasena")
    print(documento)

def validaAcceso(request):
    print("Hola Entre a validar el acceso Principal")

    username = request.POST["username"]
    print(username)
    contrasena = request.POST["password"]
    perfil = request.POST["seleccion1"]
    print(contrasena)
    print(perfil)
    context = {}
    context['documento'] = username
    print (context['documento'])

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM planta_tiposPlanta"
    cur.execute(comando)
    print(comando)

    perfiles = []
    context = {}

    for id, nombre in cur.fetchall():
        perfiles.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(perfiles)

    context['Perfiles'] = perfiles

    miConexion0 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur0 = miConexion0.cursor()
    comando = "select p.nombre nombre from planta_planta p where p.documento =' " + username + "'"
    cur0.execute(comando)

    planta = []

    for nombre in cur0.fetchall():
        planta.append({'nombre': nombre})


    if planta == []:


        context['Error'] = "Personal invalido ! "


        miConexion0.close()

        return render(request, "accesoPrincipal.html", context)

    else:
        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
        cur1 = miConexion1.cursor()
        comando = "select p.contrasena contrasena from planta_planta p where p.documento =' " + username + "'" + " AND contrasena = '" + contrasena +"'"
        cur1.execute(comando)

        plantaContrasena = []

        for nombre in cur1.fetchall():
            plantaContrasena.append({'contrasena': contrasena})

        if plantaContrasena == []:
            miConexion1.close()
            context['Error'] = "Contraseña invalida ! "
            return render(request, "accesoPrincipal.html", context)
        else:


            miConexion2 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
            cur2 = miConexion1.cursor()
            comando = "select perf.id_perfilplanta_id perfil from planta_planta p , planta_perfilesplanta perf where p.documento =' " + username + "'" + " AND p.documento = perf.documento  AND  perf.id_perfilPlanta_id= " + perfil
            cur2.execute(comando)
            print (comando)
            perfil = []

            for perfil in cur2.fetchall():
                plantaContrasena.append({'perfil': perfil})


            if perfil == []:
                miConexion0.close()
                miConexion1.close()
                miConexion2.close()
                context['Error'] = "Perfil No autorizado ! "
                return render(request, "accesoPrincipal.html", context)


            else:
                print("passe")

                print (perfil[0])

                if (perfil[0] == 1):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuMedico.html", context)
                if (perfil[0] == 2):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuEnfermero.html", context)
                if (perfil[0] == 3):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuAuxiliar.html", context)
                if (perfil[0] == 4):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuCitasMedicas.html")
                if (perfil[0] == 5):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuFacturacion.html", context)
                if (perfil[0] == 6):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "menuAdmisiones.html", context)

    return render(request, "menuMedico.html",context)




def salir(request):
    print("Voy a Salir")

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable1')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM planta_tiposPlanta"
    cur.execute(comando)
    print(comando)

    perfiles = []
    context = {}

    for id, nombre in cur.fetchall():
        perfiles.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(perfiles)

    context['Perfiles'] = perfiles

    return render(request, "accesoPrincipal.html", context)



def reconocerAudio(request):
    print ("Entre a Reconocer audio")
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())

    with sr.Microphone(device_index=0) as source:  # use the default microphone as the audio source
        print("Speak Please")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  # listen for the first phrase and extract it into audio data
        print ("pase")
    try:
            print("No haga nada")
            # print("You said " + r.recognize_google(audio , language = 'en-IN', show_all = True))  # recognize speech using Google Speech Recognition
            #text = r.recognize_google(audio, language = 'es-CO', show_all = True )
            text = r.recognize_google(audio,language = 'es-CO', show_all=True)
            print('You said: {}'.format(text))
            frutas = text.keys()
            print(frutas)

            for info in frutas.keys():
                print(info)



    except LookupError:  # speech is unintelligible
               print("Could not understand audio")

    return render(request, "home.html")


def leeAudio(request):
    print("Entre a leer audio")

    r = sr.Recognizer()
    with sr.WavFile("test.wav") as source:  # use "test.wav" as the audio source
     audio = r.record(source)  # extract audio data from the file

    try:
      print("Transcription: " + r.recognize_google(audio))  # recognize speech using Google Speech Recognition
    except LookupError:  # speech is unintelligible
      print("Could not understand audio")

    return render(request, "home.html")

def reproduceAudio(request):

    print ("Entre al Audio")
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    return redirect('/menu/')





