from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact, name='contact'),
    path('view/<int:id>', views.view, name='contact_view'),
    path('edit/<int:id>', views.edit, name='contact_edit'),
    path('create/', views.create, name='contact_create'),
    path('delete/', views.delete, name='contact_delete'),
]
