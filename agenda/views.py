from django.shortcuts import render
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from todo.models import Todo

@login_required
def index(request):
    # Obtener el número de contactos y tareas del usuario actual
    num_contactos = Contact.objects.all().count()
    num_tareas = Todo.objects.all().count()
    return render(request, 'index.html', {'num_contactos': num_contactos, 'num_tareas': num_tareas})