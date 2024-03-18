from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo, MyEvent
from .forms import TodoForm
from django.contrib import messages
import os
from django.conf import settings
from schedule.models import Event




# Create your views here.

def todo(request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search',''))
    events = Event.objects.all()  # Obtener todos los eventos
    return render(request, 'todo/index.html', {'todos': todos, 'events': events})

def view(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/detail.html', {'todo': todo})
    
def edit(request, id):
    contact = Todo.objects.get(id=id)
    if request.method == 'POST':
        formulario = TodoForm(request.POST, request.FILES, instance=contact)  # agrega request.FILES
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tarea actualizada con éxito")
            return redirect('todo')    
    else:
        formulario = TodoForm(instance=contact)
    return render(request, 'todo/edit.html', {'formulario':formulario, 'id':id})


def create(request):
    if request.method == "POST":
        formulario = TodoForm(request.POST, request.FILES)
        if formulario.is_valid():
            # Crear la carpeta media/images si no existe
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'images'), exist_ok=True)
            tarea = formulario.save()
            evento = MyEvent.objects.create(title=tarea.title, start=tarea.date, end=tarea.estimated_end, todo=tarea)
            messages.success(request, "Tarea creada con éxito")
            return redirect('todo')
    else:
        formulario = TodoForm()
    return render(request, 'todo/create.html', {"formulario": formulario})


def delete(request):
    if request.method == 'POST':
        formulario_id = request.POST.get('todo_id')
        try:
            tarea = Todo.objects.get(id=formulario_id)
            tarea.delete()
            # Puedes redirigir al usuario a una página de éxito o cualquier otra página que desees.
            messages.success(request, "Tarea eliminado con éxito")
            return redirect('todo')
        except Todo.DoesNotExist:
            messages.success(request, "La tarea No existe")

    return render(request, 'todo/index.html',{})



