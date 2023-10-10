from fastapi import APIRouter
from Functions import ListaPessoas, sortearBolean, usuarios

router = APIRouter()


@router.get("/")
async def select_all_random():
    """ Seleciona e retorna 100 pessoas por padrão, valores de [importante, lido, lixeira, anexo]
    sortidos entre True e False """

    response = usuarios(sortear=True)

    return {'success': True, 'data': response}


@router.get("/select_all")
async def select_all():
    """ Seleciona e retorna 100 pessoas por padrão, valores de [importante, lido, lixeira, anexo]
    igual a False """

    response = usuarios()

    return {'success': True, 'data': response}


@router.get("/select_random/{num}")
async def select_chosen_quantity_random(num: int):
    """ Passar quantidade de pessoas desejadas por parametro, valores de [importante, lido, lixeira, anexo]
    sortidos entre True e False"""

    num = int(num)

    response = usuarios(num, sortear=True)

    return {'success': True, 'data': response}


@router.get("/select_all/{num}")
async def select_chosen_quantity(num: int):
    """ Passar quantidade de pessoas desejadas por parametro, valores de [importante, lido, lixeira, anexo]
    igual a False"""

    num = int(num)

    response = usuarios(num)

    return {'success': True, 'data': response}


