from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.view, name='todo_view'),
    path('edit/<int:id>', views.edit, name='todo_edit'),
    path('create/', views.create, name='todo_create'),
    path('delete/', views.delete, name='todo_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

