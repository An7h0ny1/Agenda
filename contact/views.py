from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def contact(request):
    search_query = request.GET.get('search', '')
    if search_query:
        contacts = Contact.objects.filter(name__contains= search_query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contactos':contacts})

def view(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact/detail.html', { 'contacto': contact})

def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        formulario = ContactForm(request.POST, instance=contact)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contacto actualizado con éxito")
            return redirect('contact')    
    else:
        formulario = ContactForm(instance=contact)
    return render(request, 'contact/edit.html', {'formulario':formulario, 'id':id})
    
def create(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contacto creado con éxito")
            return redirect('contact')    
    else:
        formulario = ContactForm()
    return render(request, 'contact/create.html', {'formulario':formulario})


def delete(request):
    if request.method == 'POST':
        contacto_id = request.POST.get('contacto_id')
        try:
            contacto = Contact.objects.get(id=contacto_id)
            contacto.delete()
            # Puedes redirigir al usuario a una página de éxito o cualquier otra página que desees.
            messages.success(request, "Contacto eliminado con éxito")
            return redirect('contact')
        except Contact.DoesNotExist:
            messages.success(request, "Contacto No existe")

    return render(request, 'contact/index.html',{})
