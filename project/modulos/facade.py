from typing import List
from project.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados pela ordem definida
    :return:
    """

    return list(Modulo.objects.order_by('order').all())
