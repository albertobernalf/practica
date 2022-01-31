from django.shortcuts import render
import MySQLdb
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from django.views.generic import ListView, CreateView, TemplateView
from .forms import crearAdmisionForm

# Create your views here.


def menuAcceso(request):
    print("Ingreso a acceso")


    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []


    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes



    return render(request, "accesoPrincipal.html", context)



def validaAcceso(request):
    print("Hola Entre a validar el acceso Principal")

    username = request.POST["username"]
    print("username = ", username)
    contrasena = request.POST["password"]
    perfilConseguido = request.POST["seleccion1"]
    sede = request.POST["seleccion2"]
    Sede = sede
    print("Sede Mayuscula = ", Sede)
    print(contrasena)
    print("perfil= ", perfilConseguido)
    print("sede= ", sede)
    context = {}
    context['Documento'] = username
    context['Perfil'] = perfilConseguido
    context['Sede'] = sede

    # Variables que tengo en context : Documento, Perfil , Sede,   sedes ,NombreSede

    print (context['Documento'])

    # Consigo la sede Nombre

    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur = miConexion.cursor()
    comando = "SELECT nombre   FROM sitios_sedesClinica WHERE id ='" + sede + "'"
    cur.execute(comando)
    print(comando)

    nombreSedes = []

    for nombre  in cur.fetchall():
        nombreSedes.append({'nombre': nombre})

    miConexion.close()
    print(nombreSedes)
    nombresede1 = nombreSedes[0]


    context['NombreSede'] = nombresede1


    # esta consulta por que se pierde de otras pantallas

    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes


    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM planta_tiposPlanta"
    cur.execute(comando)
    print(comando)

    perfiles = []


    for id, nombre in cur.fetchall():
        perfiles.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(perfiles)

    context['Perfiles'] = perfiles

    miConexion0 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur0 = miConexion0.cursor()
    comando = "select p.nombre nombre from planta_planta p where p.documento ='" + username + "'"
    cur0.execute(comando)
    print(comando)
    planta = []

    for nombre in cur0.fetchall():
        planta.append({'nombre': nombre})


    if planta == []:


        context['Error'] = "Personal invalido ! "
        print("Entre por personal No encontrado")

        miConexion0.close()

        return render(request, "accesoPrincipal.html", context)

    else:
        miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
        cur1 = miConexion1.cursor()
        comando = "select p.contrasena contrasena from planta_planta p where p.documento ='" + username + "'" + " AND contrasena = '" + contrasena +"'"
        cur1.execute(comando)

        plantaContrasena = []

        for nombre in cur1.fetchall():
            plantaContrasena.append({'contrasena': contrasena})

        if plantaContrasena == []:
            miConexion1.close()
            context['Error'] = "Contraseña invalida ! "
            return render(request, "accesoPrincipal.html", context)
        else:


            miConexion2 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
            cur2 = miConexion1.cursor()
            comando = "select perf.tiposPlanta_id  perfil from planta_planta p , planta_perfilesplanta perf , planta_tiposPlanta tp where p.sedesClinica_id ='" + str(sede) + "' AND p.documento =  '" + str(username) + "' AND tp.id =perf.tiposPlanta_id AND  perf.tiposPlanta_id = " + str(perfilConseguido)
            print(comando)
            cur2.execute(comando)

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

                ingresos = []

                miConexionx = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curx = miConexionx.cursor()

              #  detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.serviciosActual_id = dep.servicios_id AND i.serviciosActual_id = ser.id  AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id= '" +  str(Sede) + "' AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id"

                #detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.serviciosActual_id = dep.servicios_id AND i.serviciosActual_id = ser.id  AND i.dependenciasActual_id = dep.id AND  i.dependenciasIngreso_id = dep.id AND i.sedesClinica_id= '" + str( Sede) + "' AND dep.sedesClinica_id = i.sedesClinica_id AND i.sedesClinica_id = ser.sedesClinica_id AND deptip.id = dep.dependenciasTipo_id  AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and diag.id = i.dxactual_id"
                detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id= '" + str(Sede) + "'  AND i.sedesClinica_id = ser.sedesClinica_id AND deptip.id = dep.dependenciasTipo_id and dep.servicios_id = ser.id AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and u.id = i.documento_id and diag.id = i.dxactual_id"
                print(detalle)

                curx.execute(detalle)

                for tipoDoc, documento, nombre, consec, fechaIngreso, fechaSalida, servicioNombreIng, camaNombreIng, dxActual in curx.fetchall():
                    ingresos.append({'tipoDoc': tipoDoc, 'Documento': documento, 'Nombre': nombre, 'Consec': consec,
                                     'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,
                                     'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng,
                                     'DxActual': dxActual})

                miConexionx.close()
                print(ingresos)
                context['Ingresos'] = ingresos

                # Combo de Servicios
                miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curt = miConexiont.cursor()
                comando = "SELECT id ,nombre FROM clinico_Servicios where sedesClinica_id = '" + str(Sede) +"'"
                curt.execute(comando)
                print(comando)

                servicios = []
                servicios.append({'id':'' , 'nombre': ''})

                for id, nombre in curt.fetchall():
                    servicios.append({'id': id, 'nombre': nombre})

                miConexiont.close()
                print(servicios)

                context['Servicios'] = servicios

                # Fin combo servicios

                # Combo TiposDOc
                miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curt = miConexiont.cursor()
                comando = "SELECT id ,nombre FROM usuarios_TiposDocumento "
                curt.execute(comando)
                print(comando)

                tiposDoc = []
                tiposDoc.append({'id': '', 'nombre': ''})



                for id, nombre in curt.fetchall():
                    tiposDoc.append({'id': id, 'nombre': nombre})

                miConexiont.close()
                print(tiposDoc)

                context['TiposDoc'] = tiposDoc

                # Fin combo TiposDOc

                # Combo Habitaciones
                miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curt = miConexiont.cursor()
                comando = "SELECT id ,nombre FROM sitios_dependencias where sedesClinica_id = '" + str(Sede) +"' AND dependenciasTipo_id = 1"
                curt.execute(comando)
                print(comando)

                habitaciones = []

                for id, nombre in curt.fetchall():
                    habitaciones.append({'id': id, 'nombre': nombre})

                miConexiont.close()
                print(habitaciones)

                context['Habitaciones'] = habitaciones

                # Fin combo Habitaciones

                # Combo Especialidades
                miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curt = miConexiont.cursor()
                comando = "SELECT id ,nombre FROM clinico_Especialidades"
                curt.execute(comando)
                print(comando)

                especialidades = []
                especialidades.append({'id': '', 'nombre': ''})


                for id, nombre in curt.fetchall():
                    especialidades.append({'id': id, 'nombre': nombre})

                miConexiont.close()
                print(especialidades)

                context['Especialidades'] = especialidades

                # Fin combo Especialidades

                # Combo Medicos
                miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
                curt = miConexiont.cursor()
                comando = "SELECT p.id id, p.nombre  nombre FROM planta_planta p ,  planta_perfilesplanta perf WHERE perf.sedesClinica_id = '" + str(Sede) + "' AND perf.tiposPlanta_id = 6 "

                curt.execute(comando)
                print(comando)

                medicos = []
                medicos.append({'id': '', 'nombre': ''})


                for id, nombre in curt.fetchall():
                    medicos.append({'id': id, 'nombre': nombre})

                miConexiont.close()
                print(medicos)

                context['Medicos'] = medicos

                # Fin combo Medicos


                print("passe")

                print (perfil[0])

                if (perfil[0] == 1):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    print("voy para ")
                    return render(request, "clinico/menuMedico.html", context)
                if (perfil[0] == 2):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "clinico/menuEnfermero.html", context)
                if (perfil[0] == 3):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "clinico/menuAuxiliar.html", context)
                if (perfil[0] == 4):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "citasMedicas/menuCitasMedicas.html")
                if (perfil[0] == 5):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "facturacion/menuFacturacion.html", context)

                if (perfil[0] == 6):
                    miConexion0.close()
                    miConexion1.close()
                    miConexion2.close()
                    return render(request, "admisiones/panelHospAdmisionesBravo.html", context)

    return render(request, "menuMedico.html",context)


def salir(request):
    print("Voy a Salir")

    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur = miConexion.cursor()
    comando = "SELECT id ,nombre FROM sitios_sedesClinica"
    cur.execute(comando)
    print(comando)

    sedes = []

    for id, nombre in cur.fetchall():
        sedes.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(sedes)

    context['Sedes'] = sedes





    return render(request, "accesoPrincipal.html", context)



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
    context = {}

    if (contrasenaNueva2 != contrasenaNueva):
        dato = "No coinciden las contraseñas ! "
        context['Error'] = "No coincideln las contraseñas ! "
        print(context)

        return HttpResponse(dato)


    miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur1 = miConexion1.cursor()
    comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "'"
    print(comando)
    cur1.execute(comando)

    UsuariosHc = []

    for documento, contrasena in cur1.fetchall():
        UsuariosHc = {'username': documento, 'contrasena': contrasena}

    miConexion1.close()
    print(UsuariosHc)

    if UsuariosHc == []:

        dato = "Personal invalido ! "
        context['Error'] = "Personal invalido ! "
        print(context)

        return HttpResponse(dato)
        #return render(request, "accesoPrincipal.html", context)

    else:
        miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
        cur1 = miConexion1.cursor()
        comando = "SELECT documento,contrasena FROM planta_planta WHERE documento = '" + str(username) + "' AND contrasena = '" + str(contrasenaAnt) + "'"
        print(comando)
        cur1.execute(comando)

        ContrasenaHc = []
        for documento, contrasena in cur1.fetchall():
            ContrasenaHc = {'username': documento, 'contrasena': contrasena}
        miConexion1.close()

        if ContrasenaHc == []:
            dato = "Contraseña Invalida ! "
            context['Error'] = "Contraseña Invalida ! "
            print(context)

            return HttpResponse(dato)

        else:

            miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
            cur1 = miConexion1.cursor()
            comando = "UPDATE planta_planta SET contrasena = '" +  str(contrasenaNueva) + "' WHERE documento = '" + str(username) + "'"
            print(comando)
            cur1.execute(comando)
            miConexion1.commit()
            miConexion1.close()
            context['Error'] = "Contraseña Actualizada ! "
            dato = "Contraseña Actualizada !"
            print(context)
            #return HttpResponse(context, safe=False)
            return HttpResponse(dato)
            #return render(request, "accesoPrincipal.html", context)


    #return JsonResponse(UsuariosHc, safe=False)

def Modal(request, username, password):

        print("Entre a Modal")
        print(username)
        print(password)

        miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
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


def admHospProvisional(request,Documento, Perfil,  Sede, Servicio):

    print("admHospProvisional")
    print(Documento)
    context1 = {}
    context1['Documento'] = Documento
    context1['Perfil'] = Perfil
    print (Perfil)
    context1['Sede'] = Sede
    print ("En admHospProvisional la sede = a ", Sede)
    print("En admHospProvisional la sede Context = a ", context1['Sede'] )
    #context1['NombreSede'] = NombreSede
    context1['Servicio'] = Servicio




    return render(request, "admisiones/panelHospAdmisiones.html", context1)



def buscarAdmision(request):
    context = {}

    print("Entre Buscar Admision" )
    BusHabitacion = request.POST["busHabitacion"]
    BusTipoDoc = request.POST["busTipoDoc"]
    BusDocumento = request.POST["busDocumento"]
    BusDesde = request.POST["busDesde"]
    BusHasta = request.POST["busHasta"]
    BusEspecialidad = request.POST["busEspecialidad"]
    BusMedico = request.POST["busMedico"]
    BusServicio = request.POST["busServicio"]
    BusPaciente = request.POST["busPaciente"]

    Sede = request.POST["Sede"]
    print("otra sede = ", Sede)

    print("BusHabitacion= ", BusHabitacion)
    print("BusTipoDoc=", BusTipoDoc)
    print("BusDocumento=" , BusDocumento)
    print("BusDesde=", BusDesde)
    print("BusHasta=", BusHasta)
    print("La sede es = " , Sede)
    print("El busServicio = ", BusServicio)
    print("El busEspecialidad = ", BusEspecialidad)
    print("El busSMedico = ", BusMedico)
    print("El busSMedico = ", BusPaciente)

    ingresos = []


    # Combo de Servicios
    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Servicios where sedesClinica_id = '" + str(Sede) + "'"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios
    context['Sede'] = Sede

    # Fin combre servicios

    # Combo TiposDOc
    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM usuarios_TiposDocumento"
    curt.execute(comando)
    print(comando)

    tiposDoc = []
    tiposDoc.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDoc.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDoc)

    context['TiposDoc'] = tiposDoc

    # Fin combo TiposDOc


    # Combo Habitaciones
    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM sitios_dependencias where sedesClinica_id = '" + str(Sede) +"' AND dependenciasTipo_id = 1"
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})


    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    context['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    # Combo Especialidades
    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Especialidades"
    curt.execute(comando)
    print(comando)

    especialidades = []
    especialidades.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidades)

    context['Especialidades'] = especialidades

    # Fin combo Especialidades

    # Combo Medicos
    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT p.id id, p.nombre  nombre FROM planta_planta p ,  planta_perfilesplanta perf WHERE perf.sedesClinica_id = '" + str(Sede) +"' AND perf.tiposPlanta_id = 6 "
    curt.execute(comando)
    print(comando)

    medicos = []
    medicos.append({'id': '', 'nombre': ''})


    for id, nombre in curt.fetchall():
        medicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicos)

    context['Medicos'] = medicos

    # Fin combo Medicos


    # Busco Nombre de Habitacion

    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_dependencias d WHERE d.id = '" + str(BusHabitacion) + "'"
    curt.execute(comando)
    print(comando)

    NombreHabitacion = ""


    for id, nombre in curt.fetchall():
        NombreHabitacion = nombre

    miConexiont.close()
    print("NombreHabitacion = ", NombreHabitacion)


    # Fin busco nombre de habitacion



    miConexion1 = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    cur1 = miConexion1.cursor()

 #   detalle = "SELECT i.tipoDoc_id tipoDoc, i.documento_id documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, serviciosIng_id,  dependenciasIngreso_id , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id = '" +    str(Sede) +"'"
  #  detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.serviciosActual_id = dep.servicios_id AND i.serviciosActual_id = ser.id  AND i.dependenciasActual_id = dep.id AND  i.dependenciasIngreso_id = dep.id AND i.sedesClinica_id= '" + str(Sede) + "' AND dep.sedesClinica_id = i.sedesClinica_id AND i.sedesClinica_id = ser.sedesClinica_id AND deptip.id = dep.dependenciasTipo_id  AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and diag.id = i.dxactual_id"
    detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id= '" + str(Sede) + "'  AND i.sedesClinica_id = ser.sedesClinica_id AND deptip.id = dep.dependenciasTipo_id and dep.servicios_id = ser.id AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and u.id = i.documento_id and diag.id = i.dxactual_id"


    print(detalle)

    if BusServicio != "":
      detalle = detalle + " AND  ser.id = '" + str(BusServicio) + "'"
    print(detalle)

    if BusDesde != "":
        detalle = detalle +  " AND i.fechaIngreso >= '" + str(BusDesde) +"'"
        print (detalle)

    if BusHasta != "":
        detalle = detalle + " AND i.fechaIngreso <=  '" + str(BusHasta) + "'"
        print(detalle)

    if BusHabitacion != "":
        detalle = detalle + " AND dep.nombre = '" + str(NombreHabitacion) + "'"
        print(detalle)

    if BusTipoDoc != "":
            detalle = detalle + " AND i.tipoDoc_id= '" + str(BusTipoDoc) + "'"
            print(detalle)

    if BusDocumento != "":
                detalle = detalle + " AND u.documento= '" + str(BusDocumento) + "'"
                print(detalle)

    if BusPaciente != "":
        detalle = detalle + " AND u.nombre like '%" + str(BusPaciente) + "%'"
        print(detalle)

    if BusMedico != "":
        detalle = detalle + " AND i.medicoActual_id = '"  + str(BusMedico) + "'"
        print(detalle)

    cur1.execute(detalle)



    for tipoDoc, documento_id, nombre , consec, fechaIngreso,  fechaSalida, servicioNombreIng, camaNombreIng, dxActual  in cur1.fetchall():

        ingresos.append ({'tipoDoc' : tipoDoc, 'Documento': documento_id, 'Nombre': nombre , 'Consec': consec, 'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida, 'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng, 'DxActual': dxActual})

    miConexion1.close()
    print(ingresos)
    context['Ingresos'] = ingresos




    return render(request, "admisiones/panelHospAdmisionesBravo.html", context)




def buscarHabitaciones(request):
    context = {}
    Serv = request.GET["Serv"]
    Sede = request.GET["Sede"]
    print ("Entre buscar habitaciones servicio =",Serv)
    print ("Sede = ", Sede)


    # Busco la habitaciones de un Servicio

    miConexiont = MySQLdb.connect(host='192.168.0.13', user='root', passwd='', db='vulnerable2')
    curt = miConexiont.cursor()
    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_dependencias d , clinico_servicios cl WHERE d.sedesclinica_id = '" + str(Sede) + "' and  d.dependenciastipo_id=1 and cl.nombre ='" + str(Serv.lstrip()) + "' AND  d.sedesClinica_id = cl.sedesClinica_id and d.servicios_id = cl.id"
    curt.execute(comando)
    print(comando)

    Habitaciones =[]


    for id, nombre in curt.fetchall():
        Habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(Habitaciones)
    context['Habitaciones'] = Habitaciones

    return JsonResponse(json.dumps(Habitaciones), safe=False)

class crearAdmision(TemplateView):
    print("Entre a Craer Admision")
    template_name = 'admisiones/crearAdmision.html'
    print("Entre a Registrar Admision")

    def post(self, request, *args, **kwargs):
        print("Entre POST")
        data = {}
        try:
            print("Entre try")
            if 'action' in request.POST:
                action = request.POST['action']
                id = request.POST['id']
            else:
                print("Falsa action")
                action = False
            print(action)
            print(id)

            action = request.POST.get('action', False)

            if action == 'BuscaExamenes':
                print("Entre Action")
                data = []
                for s in Examenes.objects.all().filter(id_TipoExamen=request.POST["id"]):
                    data.append({'id': s.id, 'nombre': s.nombre})
                    print(data[0])
            else:
                data[0] = "Ha ocurrido un error"

            if action == 'BuscaEspecialidad':
                print("Entre Action especialidad")
                print(id)
                data = []
                for s in EspecialidadesMedicos.objects.all().filter(id_especialidad=request.POST["id"]):
                    medico = Medicos.objects.get(nombre=s.id_medico)

                    data.append({'id': s.id, 'nombre': medico.nombre})
                    print(data[0])
            else:
                data[0] = "Ha ocurrido un error"


        except Exception as e:
            print("Exception")
            #data[0] = atrr(e)

        print("me devuelvo con ")

        return HttpResponse(json.dumps(data))

    def get_context_data(self, **kwargs):
        print("Entre a Contexto")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi gran Template'
        context['form'] = crearAdmisionForm
   #     context['form2'] = historiaExamenesForm
        print("Se supone voya a cargar la forma")
        print (context)
        return context


def crearResponsables(request):
    print("Entre crear Responsables")
    pass