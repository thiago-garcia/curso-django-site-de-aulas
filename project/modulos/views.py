from django.shortcuts import render
from project.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    if slug == 'introducao':
        return render(request, 'modulos/modulo_detalhe.html')


def aula(request, slug):
    if slug == 'aula-inicial':
        return render(request, 'modulos/aula_detalhe.html')
