from typing import List
from project.turmas.models import Turma


def listar_turmas_ordenadas() -> List[Turma]:
    """
    Lista as turmas ordenadas pelo inicio
    """
    return list(Turma.objects.order_by('inicio').all())
