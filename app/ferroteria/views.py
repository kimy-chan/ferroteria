from gzip import READ
import re
from django.shortcuts import HttpResponse, render , redirect
from django.contrib.auth.decorators import login_required
from .models import herramienta
from .models import Pinturas
from .forms import FormularioHerramientas
from .forms import FormularioPinturas



# Create your views here.
@login_required
def administracion(request):
    herramientas = herramienta.objects.all()
    totalDeHerramientas =herramienta.objects.count()
    totalDePinturas = Pinturas.objects.count()
   
    pinturas = Pinturas.objects.all()
    return render(request, 'administracion.html',{'herramientas':herramientas, 'pinturas':pinturas,
    'totalHerramienta':totalDeHerramientas , 'totalPinturas': totalDePinturas
    })

def index(request):
    return render(request,'inicio.html')

def mostrarDatosPintutas(request):
    pinturas =Pinturas.objects.all()
    return render(request,'pinturas.html', {'pinturas':pinturas})

def mostrarDatosHerramientas(request):
    herramientas = herramienta.objects.all()
    return render(request,'herramientas.html', {'herramientas':herramientas})


@login_required
def ingresarDatosHerramientas(request):
    formularioH = FormularioHerramientas(request.POST or None, request.FILES or None)
    if formularioH.is_valid():
        formularioH.save()
        return redirect('administracion')
    return render (request,'agreagarH.html',{'formulario':formularioH})

@login_required
def ingresarDAtosPinturas(request):
    FormularioP = FormularioPinturas(request.POST or None, request.FILES or None)
    if FormularioP.is_valid():
        FormularioP.save()
        return redirect('administracion')
    return render(request,'agregarP.html',{'formulario':FormularioP })
@login_required    
def borrarH(request, id):
    herramientas = herramienta.objects.get(id=id)
    herramientas.delete()
    return redirect('administracion') 
@login_required    
def borrarP(request, id):
    pintutas = Pinturas.objects.get(id=id)
    pintutas.delete()
    return redirect('administracion')
@login_required    
def editarH(request, id):
    herramientas = herramienta.objects.get(id=id)
    form = FormularioHerramientas(request.POST or None , request.FILES or None, instance=herramientas)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('administracion')
    return render(request,'formularioE.html',{'formulario':form})
@login_required   
def editarP(request,id):
    pinturas = Pinturas.objects.get(id=id)
    form= FormularioPinturas(request.POST or None, request.FILES or None, instance=pinturas)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('administracion')
    return render(request,'formularioE.html',{'formulario':form})
