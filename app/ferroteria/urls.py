

from django.urls import path

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('administracion',views.administracion, name="administracion"),
    path('', views.index, name='inicio'),
    path('herramientas',views.mostrarDatosHerramientas, name='herramientas'),
    path('pinturas',views.mostrarDatosPintutas, name='pinturas'),
    path('ingresarDatosH',views.ingresarDatosHerramientas, name='ingresarH'),
    path('agregarDatosP', views.ingresarDAtosPinturas, name='agregarP'),
    path('eliminar/<int:id>',views.borrarH , name='eliminar'),
    path('eliminarP/<int:id>',views.borrarP,name='eliminarP'),
    path('editar/<int:id>', views.editarH, name='editarH'),
    path('editarP/<int:id>', views.editarP, name='editarP')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
