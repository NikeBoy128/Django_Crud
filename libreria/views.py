
import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Modelo_libros,Genero
from .forms import LibroForm,GeneroForm


def index(request):  
    libros=Modelo_libros.objects.all()
    return render(request,'libros/indexlibros.html',{'libros':libros} )

def crearlibro(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():      
        formulario.save()    
        return redirect('index')
    return render(request,'libros/crear.html',{'formulario':formulario})

def editarlibro(request,id):
    libro=Modelo_libros.objects.get(id=id)
    formulario=LibroForm(request.POST or None,request.FILES or None,instance=libro)
    if formulario.is_valid():      
        formulario.save()    
        return redirect('index')    
    return render(request,'libros/editar.html',{'formulario':formulario})

def indexgenero(request):
    generos=Genero.objects.all()
    return render(request,'libros/indexgenero.html',{'generos':generos} )

def creargenero(request):
    formulario = GeneroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():      
        formulario.save()    
        return redirect('indexgenero')
    return render(request,'libros/creargenero.html',{'formulario':formulario})

def editargenero(request,id):
    genero=Genero.objects.get(id=id)
    formulario=GeneroForm(request.POST or None,instance=genero)  
    if formulario.is_valid():      
        formulario.save()    
        return redirect('indexgenero')  
    return render(request,'libros/editargenero.html',{'formulario':formulario})
