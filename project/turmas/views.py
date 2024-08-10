from django.shortcuts import render
from project.turmas import facade


def indice(request):
    turmas = facade.listar_turmas_ordenadas()

    return render(request, 'turmas/indice.html', {'turmas': turmas})
