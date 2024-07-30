from django.shortcuts import render


def indice(request):
    return render(request, 'modulos/indice.html')


def detalhe(request, slug):
    if slug == 'introducao':
        return render(request, 'modulos/modulo_detalhe.html')


def aula(request, slug):
    if slug == 'aula-inicial':
        return render(request, 'modulos/aula_detalhe.html')
