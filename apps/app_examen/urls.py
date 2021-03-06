from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index_view,name='index_view'),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'app_examen/login.html'}, name='login'),
    url(r'^signup/$',Signup.as_view(),name='signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^add_materia/$',register_materia.as_view(),name='add_materia'),
    url(r'^signup_a/$',Signup_Alumno.as_view(),name='signup_a'),
    url(r'^register_preguntas',pregunta.as_view(),name='register_preguntas'),
    url(r'^register_respuesta',respuesta.as_view(),name='register_respuesta'),
    #url(r'^prueva/$',prueva.as_view(),name='prueva'),
    #url(r'^prueva2/$',prueva2.as_view(),name='prueva2'),
]