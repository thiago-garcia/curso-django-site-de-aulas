from django.urls import path

from project.modulos import views


app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('', views.indice, name='indice'),
]
