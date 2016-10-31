from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import UserForm, UserFormAlumno, respuestas_form,Preguntas_form
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import Profesor,Materia,Alumno,Preguntas,Respuesta
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
    return render(request,'app_examen/index.html')

def login_view(request):
    return render(request,'app_examen/login.html')

class Signup(FormView):
    template_name = 'app_examen/signup.html'
    form_class = UserForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        user = form.save()
        p = Profesor()
        p.user_perfil = user
        p.name = form.cleaned_data['name']
        p.mail = form.cleaned_data['mail']
        p.save()
        return super(Signup, self).form_valid(form)

class Signup_Alumno(FormView):
    template_name = 'app_examen/Signup_a.html'
    form_class = UserFormAlumno
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        user = form.save()
        p = Alumno()
        p.user_perfil = user
        p.mail = form.cleaned_data['mail']
        p.name = form.cleaned_data['name']
        p.n_control = form.cleaned_data['n_control']
        p.save()
        return super(Signup_Alumno,self).form_valid(form)


class register_materia(CreateView):
    template_name = 'app_examen/register_materia.html'
    model = Materia
    fields = ['materia','serie','profesor']
    success_url = reverse_lazy('index_view')

class pregunta(CreateView):
    template_name = 'app_examen/pregunta_respuesta.html'
    model = Preguntas
    fields = ['pregunta','dificultad','valor']
    success_url = reverse_lazy('register_respuesta')

class respuesta(CreateView):
    template_name = 'app_examen/respueta_pregunta.html'
    model = Respuesta
    fields = ['opcion','corecta','pregun']
    success_url = reverse_lazy('index_view')

    def get_context_data(self, **kwargs):
        ctx = super(respuesta,self).get_context_data(**kwargs)
        ctx['pre'] = Preguntas.objects.all()
        return ctx


#######################################################
#Borar
#class prueva(FormView):
#    template_name = 'app_examen/p.html'
#    form_class = Preguntas_form
#    success_url = reverse_lazy('prueva2')
#    def form_valid(self, form):
#        p = Preguntas()
#        p.pregunta = form.cleaned_data['pregunta']
#        p.dificultad = form.cleaned_data['dificultad']
#        p.valor = form.cleaned_data['valor']
#        p.save()
#        return super(prueva,self).form_valid(form)

#class prueva2(FormView):
#    template_name = 'app_examen/p2.html'
#    form_class = respuestas_form
#    success_url = reverse_lazy('index_view')
#    def form_valid(self, form):
#        p = Respuesta()
#        p.opcion  = form.cleaned_data['opcion']
#        p.corecta = form.cleaned_data['corecta']
        #instance = get_object_or_404(Preguntas)
#        p.pregun  = form.cleaned_data['pregun']
#        p.save()
#        return super(prueva2,self).form_valid(form)

#    def get_context_data(self, **kwargs):
#        ctx = super(prueva2,self).get_context_data(**kwargs)
#        ctx['pre'] = Preguntas.objects.all()
#        return ctx

class prueva(CreateView):
    template_name = 'app_examen/p.html'
    model = Preguntas
    fields = ['pregunta','dificultad','valor']
    success_url = reverse_lazy('prueva2')

class prueva2(CreateView):
    template_name = 'app_examen/p2.html'
    model = Respuesta
    fields = ['opcion','corecta','pregun']
    success_url = reverse_lazy('index_view')

    def get_context_data(self, **kwargs):
        ctx = super(prueva2,self).get_context_data(**kwargs)
        ctx['pre'] = Preguntas.objects.all()
        return ctx
















