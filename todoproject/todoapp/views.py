from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import TodoListItem, Contact, Proyecto
from django.core import serializers
from todoapp.forms import formTodo, formContact, formProyecto

# Create your views here.
def todoAppCreate(request):
    if request.method == 'POST':
        miFormulario = formTodo(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            IListable = TodoListItem(nota=informacion['nota'],pendiente=informacion['pendiente'])
            IListable.save()
            return render(request, 'todoapp/inicio.html')
    else:
        miFormulario=formTodo()
        return render(request, 'todoapp/CargaItem.html',{'miFormulario':miFormulario})
    
def ContactCreate(request):
    if request.method == 'POST':
        miFormulario = formContact(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            _contacto = Contact(nombre=informacion['nombre'],telefono=informacion['telefono'],correo=informacion['correo'])
            _contacto.save()
            return render(request, 'todoapp/inicio.html')
    else:
        miFormulario = formContact()
        return render(request, 'todoapp/CargaContact.html',{'miFormulario':miFormulario})

def ProjectCreate(request):
    if request.method == 'POST':
        miFormulario = formProyecto(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            _proyecto = Proyecto(nombre=informacion['nombre'],descripcion=informacion['descripcion'])
            _proyecto.save()
            return render(request, 'todoapp/inicio.html')
    else:
        miFormulario = formProyecto()
        return render(request, 'todoapp/CargaProyecto.html',{'miFormulario':miFormulario})

def todoApi(request):
    item_todos=TodoListItem.objects.all()
    return HttpResponse(serializers.serialize('json',item_todos))

def contactApi(request):
    all_contacts=Contact.objects.all()
    return HttpResponse(serializers.serialize('json',all_contacts))

def projectApi(request):
    all_project=Proyecto.objects.all()
    return HttpResponse(serializers.serialize('json',all_project))

def inicio (request):
    return render(request,'todoapp/inicio.html')