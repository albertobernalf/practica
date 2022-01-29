from django.shortcuts import render
import MySQLdb

# Create your views here.


def menuAcceso(request):
    print("Ingreso a acceso")


    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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


    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion0 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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
        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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


            miConexion2 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    miConexion = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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


    miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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
        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

            miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

        miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
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

    print("Entre Buscar Admision" )
    BusHabitacion = request.POST["busHabitacion"]
    BusTipoDoc = request.POST["busTipoDoc"]
    BusDocumento = request.POST["busDocumento"]
    BusDesde = request.POST["busDesde"]
    BusHasta = request.POST["busHasta"]
    BusEspecialidad = request.POST["busEspecialidad"]
    BusMedico = request.POST["busMedico"]
    BusServicio = request.POST["busServicio"]

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


    ingresos = []
    context = {}

    miConexion1 = MySQLdb.connect(host='192.168.0.14', user='root', passwd='', db='vulnerable2')
    cur1 = miConexion1.cursor()
  #  comando = "SELECT i.tipoDoc_id tipoDoc, i.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, serviciosIng_id,  dependenciasIngreso_id , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep  WHERE  i.tipoDoc_id = u.tipoDoc_id and i.documento  = u.documento AND u.documento = '" + str(BusDocumento) + "' AND i.sedesClinica_id = '" + str(Sede) + "'" + " AND serviciosActual_id = '" + str(Servicio) + "'  AND i.dependenciasActual_id = dep.id AND dep.nombre = '" + str(BusHabitacion) + "'"

    # Aqui encadeno el query final con todos los parametros de consultas

    detalle = "SELECT i.tipoDoc_id tipoDoc, i.documento_id documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, serviciosIng_id,  dependenciasIngreso_id , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep  WHERE "
    print(detalle)
    if BusDesde != "":
        detalle = detalle +  " i.fechaIngreso >= '" + str(BusDesde) +"'"
        print (detalle)

    if BusHasta != "":
        detalle = detalle + " AND i.fechaIngreso <=  '" + str(BusHasta) + "'"
        print(detalle)

    if Sede != "":
        detalle = detalle + " AND i.sedesClinica_id = '" + str(Sede) + "'"
        print(detalle)

  #  if BusDocumento != "":
  #      detalle = detalle + " AND i.sedesClinica_id = '" + str(Sede) + "'"
  #      print(detalle)


   # comando = "SELECT i.tipoDoc_id tipoDoc, i.documento_id documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, serviciosIng_id,  dependenciasIngreso_id , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep  WHERE  i.tipoDoc_id = u.tipoDoc_id and i.documento_id  = u.id AND i.fechaIngreso >= '" + str(
   #     BusDesde) + "' AND i.fechaIngreso <=  '" + str(BusHasta) + "'  AND i.sedesClinica_id = '" + str(
   #     Sede) + "'" + " AND serviciosActual_id = '" + str(Servicio) + "'  AND i.dependenciasActual_id = dep.id "
   # print(comando)
    cur1.execute(detalle)



    for tipoDoc, documento_id, nombre , consec, fechaIngreso,  fechaSalida, serviciosIng_id ,  dependenciasIngreso_id ,dxIngreso_id  in cur1.fetchall():

        ingresos.append ({'tipoDoc' : tipoDoc, 'Documento': documento_id, 'Nombre': nombre , 'Consec': consec, 'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida,'ServiciosIng': serviciosIng_id, 'DependenciasIngreso' : dependenciasIngreso_id, 'DxIngreso': dxIngreso_id})

    miConexion1.close()
    print(ingresos)
    context['Ingresos'] = ingresos




    return render(request, "admisiones/panelHospAdmisionesBravo.html", context)


