from fastapi import APIRouter
from Functions import ListaPessoas, sortearBolean

router = APIRouter()


@router.get("/")
async def select_all_random():
    """ Seleciona e retorna 100 pessoas por padrão, valores de [importante, lido, lixeira, anexo]
    sortidos entre True e False """

    response = ListaPessoas(sortear=True)

    return {'success': True, 'data': response}


@router.get("/select_all")
async def select_all():
    """ Seleciona e retorna 100 pessoas por padrão, valores de [importante, lido, lixeira, anexo]
    igual a False """

    response = ListaPessoas()

    return {'success': True, 'data': response}


@router.get("/select_random/{num}")
async def select_chosen_quantity_random(num: int):
    """ Passar quantidade de pessoas desejadas por parametro, valores de [importante, lido, lixeira, anexo]
    sortidos entre True e False"""

    num = int(num)

    response = ListaPessoas(num, sortear=True)

    return {'success': True, 'data': response}


@router.get("/select_all/{num}")
async def select_chosen_quantity(num: int):
    """ Passar quantidade de pessoas desejadas por parametro, valores de [importante, lido, lixeira, anexo]
    igual a False"""

    num = int(num)

    response = ListaPessoas(num)

    return {'success': True, 'data': response}


