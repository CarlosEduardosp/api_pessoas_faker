from fastapi import APIRouter
from faker import Faker

router = APIRouter()

faker = Faker('pt_BR')  # chamando a função Faker com a sigla 'pt_BR' para retornar dados em portugues


@router.get("/")
async def select_all():
    """ Seleciona e retorna 100 pessoas por padrão """

    lista_dados = []

    for i in range(100):
        dados = {
            'id': i,
            'nome': faker.name(),
            'remetente': faker.email(),
            'assunto': faker.city(),
            'mensagem': faker.text(),
            'importante': False,
            'lido': False,
            'lixeira': False
        }

        lista_dados.append(dados)

    return {'success': True, 'data': lista_dados}


@router.get("/{num}")
async def select_chosen_quantity(num: int):
    """ Passar quantidade de pessoas desejadas por parametro."""

    num = int(num)
    print(num)
    lista_dados = []

    for i in range(num):
        dados = {
            'id': i,
            'nome': faker.name(),
            'remetente': faker.email(),
            'assunto': faker.city(),
            'mensagem': faker.text(),
            'importante': False,
            'lido': False,
            'lixeira': False
        }

        lista_dados.append(dados)

    return {'success': True, 'data': lista_dados}
