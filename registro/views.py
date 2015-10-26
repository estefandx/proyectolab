from django.shortcuts import render, redirect, render_to_response, RequestContext
from proyecto.models import USUARIO, DUENO, JEFE, TRABAJADOR
from form import registro
from django.http import HttpResponse




def prueba(request):

    return  render(request,'confirmacion.html')


def editarPerfil(request,usuario_id):
    usuario = USUARIO.objects.get(pk = usuario_id)
    if request.method == 'POST':
        form = registro(request.POST, instance=usuario)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            genero = form.cleaned_data["genero"]
            password = form.cleaned_data["password"]
            tipoDocumento = form.cleaned_data["tipoDocumento"]
            numero_documento = form.cleaned_data["numero_Documento"]

            fecha_nacimiento =form.cleaned_data["fecha_nacimiento"]
            direccion = form.cleaned_data["direccion"]
            telefono = form.cleaned_data["telefono"]
            user = USUARIO.objects.create_user(first_name=first_name, last_name=last_name, email=email, genero=genero,
                                                     password=password, tipoDocumento=tipoDocumento, numero_Documento= numero_documento,
                                                     fecha_nacimiento=fecha_nacimiento, direccion=direccion,
                                                     username=numero_documento, telefono=telefono)
        user.save()
        return  redirect('correcto')
    else:
        form = registro(instance=registro)
    return render_to_response('usuario_editar.html',{'form': form},context_instance=RequestContext(request))





def crearPerfil(request):
    if request.method == 'POST':
        form = registro(request.POST)
        if form.is_valid():
            if request.user.is_superuser:
                perfilregistro = "dueno"
                tipousuario = "administrador"


            else:

             usuario = USUARIO.objects.get(username=request.user.username)
             tipousuario = usuario.tipo_usuario

        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        genero = form.cleaned_data["genero"]
        password = form.cleaned_data["password"]
        tipoDocumento = form.cleaned_data["tipoDocumento"]
        numero_documento = form.cleaned_data["numero_Documento"]

        fecha_nacimiento =form.cleaned_data["fecha_nacimiento"]
        direccion = form.cleaned_data["direccion"]
        telefono = form.cleaned_data["telefono"]



        if tipousuario == "dueno":
                perfilregistro = "jefe"
                # cargo = JEFE(documento_id=numero_documento,dueno_id=usuario.numero_Documento)
                # cargo.save() # cargo = JEFE(documento_id=numero_documento,dueno_id=usuario.numero_Documento)
                # cargo.save()


        elif tipousuario == "jefe":
            perfilregistro = "trabajador"
            # cargo = TRABAJADOR(documento_id= numero_documento, jefe_id=usuario.numero_Documento)
            # cargo.save()



        elif tipousuario == "administrador":
             perfilregistro = "dueno"



        user = USUARIO.objects.create_user(first_name=first_name, last_name=last_name, email=email, genero=genero,
                                                     password=password, tipoDocumento=tipoDocumento, numero_Documento= numero_documento,
                                                     fecha_nacimiento=fecha_nacimiento, direccion=direccion,
                                                     username=numero_documento, telefono=telefono, tipo_usuario = perfilregistro)
        user.save()
        return redirect('correcto')
    else:
        form = registro()
    return render_to_response('registro.html',{'form': form},context_instance=RequestContext(request))
    #return render(request,'registro.html',{'form':form})





























