from django.urls import path

from project.modulos import views


app_name = 'modulos'
urlpatterns = [
    path('', views.indice, name='indice'),
]
