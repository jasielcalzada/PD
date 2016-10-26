from django.contrib import admin
from .models import Profesor,Materia,Alumno,Preguntas,Respuesta,Examen
# Register your models here.
#admin.site.register(Profesor)
@admin.register(Profesor)
class Profesor_admin(admin.ModelAdmin):
    list_display = ('id','user_perfil','mail','name','categoria')

#admin.site.register(Materia)

@admin.register(Materia)
class Materia_admin(admin.ModelAdmin):
    List_display = ('id','materia','serie')

@admin.register(Alumno)
class Alumno_admin(admin.ModelAdmin):
    list_display = ('id','user_perfil','mail','name','n_control','categoria')

@admin.register(Preguntas)
class Preguntas(admin.ModelAdmin):
    list_display = ('id','pregunta','dificultad','valor')

@admin.register(Respuesta)
class Respuestas(admin.ModelAdmin):
    list_display = ('id','opcion','corecta','pregun')

@admin.register(Examen)
class Examen(admin.ModelAdmin):
    list_display = ('id','materia','profesor','alumno','unidad','pregun','respue')


