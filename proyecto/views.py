from django.shortcuts import render
from proyecto.models import USUARIO
# Create your views here.


def index(request):
    return render(request,'index.html')


def acciones(request):
    if request.user.is_superuser:
        persona = None
    else:
        persona =USUARIO.objects.get(username=request.user.username)
    return render(request,'acciones.html',{'persona':persona})