from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('libros/crearlibros',views.crearlibro,name="crearlibro"),
    path('libros/editarlibro/<int:id>/',views.editarlibro,name="editarlibro"),
    path('libros/indexgenero',views.indexgenero,name="indexgenero"),
    path('libros/creargenero',views.creargenero,name="creargenero"),
    path('libros/editargenero/<int:id>/',views.editargenero,name="editargenero"),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
