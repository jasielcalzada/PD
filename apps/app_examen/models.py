from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
# Create your models here.
class Materia(models.Model):
    materia = models.CharField(max_length=64)
    serie = models.CharField(max_length=64)
    profesor = models.CharField(max_length=64,blank=True,null=True)

    def __unicode__(self):
        return '%s %s %s'%(self.materia,self.serie,self.profesor)

class Profesor(models.Model):
    user_perfil = models.OneToOneField(User, related_name="profile")
    mail = models.EmailField()
    name = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64,null = True,default="profesor")

    def __unicode__(self):
        return '%s'%(self.user_perfil)


class Alumno(models.Model):
    user_perfil = models.OneToOneField(User, related_name="profile_a")
    mail = models.EmailField()
    name = models.CharField(max_length=64)
    n_control = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64,null=True,default="alumno")

    def __unicode__(self):
        return '%s'%(self.user_perfil)


#NO USAR ESTE

#
class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200)
    nivel = (('Facil','Facil'),('Intermedio','Intermedio'),('Dificil','Dificil'))
    dificultad = models.CharField(max_length=64,choices=nivel)
    valor = models.PositiveIntegerField( validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __unicode__(self):
        return '%s %s %d'%(self.pregunta,self.dificultad,self.valor)

class Respuesta(models.Model):
    opcion = models.CharField(max_length=200,blank=True)
    corecta = models.CharField(max_length=200,blank=True)
    pregun = models.ForeignKey(Preguntas,null=True)

    def __unicode__(self):
        return '%s %s %s'%(self.opcion,self.corecta,self.pregun)
class Examen(models.Model):
    materia = models.ForeignKey(Materia,null=True)
    profesor = models.ForeignKey(Profesor,null=True)
    alumno = models.ForeignKey(Alumno,null=True)
    unidad = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(7)],null=True)
    pregun = models.ForeignKey(Preguntas)
    respue = models.ForeignKey(Respuesta)



    def __unicode__(self):
        return '%s %s %s %d %s %s'%(self.materia,self.profesor.name,self.alumno.name,self.unidad,self.pregun,self.respue)









