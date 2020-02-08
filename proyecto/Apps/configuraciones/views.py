from django.shortcuts import render
from proyecto.Apps.configuraciones.models import *
from django.shortcuts import render,redirect,HttpResponseRedirect


def index(request):
   if 'usuario' in request.session:
       menu = Permisos.objects.filter(usuario_rol_id__id_usuario=request.session.get('usuario')).select_related('menu')
       for m in menu:
           print(m.menu.nombre)
       return render(request,'index.html',{'permisos':menu})
   else:
       return redirect('Proyecto:login')

def login(request):
   #print('llege')
    contexto = {}
    if request.method=='POST':
       usuario = Usuario.objects.filter(usuario=request.POST.get('usuario'), clave=request.POST.get('clave'))
       for u in usuario:
          if u:
             #print(u.usuario)
             request.session['usuario'] = u.id_usuario
             return redirect('Proyecto:inicio')
          else:
              contexto['Error'] = 'Claves incorrectas o cuenta inactiva'
              return render(request,'base/login.html',contexto)
    return render(request,'base/login.html')

def salir(request):
    del request.session['usuario']
    return HttpResponseRedirect('../')


def usuario(request):
  if 'usuario' in request.session:
      usuarios = ConfUsuario_rol.objects.filter()
      return render(request,'Usuario/usuario.html',{'usuarios':usuarios})

def agregar_usuario(request):
    roles = Rol.objects.filter()
    return render(request,'Usuario/Agregar_usuario.html',{'roles':roles})
