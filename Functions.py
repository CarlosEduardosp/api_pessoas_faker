from faker import Faker
import random

faker = Faker('pt_BR')  # chamando a função Faker com a sigla 'pt_BR' para retornar dados em portugues


def sortearBolean():

    lista = [True, False]
    response = random.choice(lista)

    return response


def ListaPessoas(num: int = 100, sortear: bool = False, nome: str = ''):

    if sortear:
        lista_dados = []

        usuarios()

        for i in range(num):
            dados = {
                'id': i,
                'nome_id': nome,
                'nome': faker.name(),
                'remetente': faker.email(),
                'assunto': faker.city(),
                'mensagem': faker.text(),
                'importante': sortearBolean(),
                'lido': sortearBolean(),
                'lixeira': sortearBolean(),
                'anexo': sortearBolean()
            }

            lista_dados.append(dados)

        return lista_dados

    else:
        lista_dados = []

        for i in range(num):
            dados = {
                'id': i,
                'nome_id': nome,
                'nome': faker.name(),
                'remetente': faker.email(),
                'assunto': faker.city(),
                'mensagem': faker.text(),
                'importante': False,
                'lido': False,
                'lixeira': False,
                'anexo': False
            }

            lista_dados.append(dados)

        return lista_dados


def usuarios(num: int = 100, sortear: bool = False):

    usuarios_list = []

    response = ListaPessoas(num, sortear, 'administrador')
    administrador = {
        'nome': 'Administrador',
        'login': 12345678910,
        'senha': 123456,
        'data': response
    }

    response = ListaPessoas(num, sortear, 'cliente1')
    cliente1 = {
        'nome': 'cliente1',
        'login': 123456,
        'senha': 654321,
        'data': response
    }

    response = ListaPessoas(num, sortear, 'cliente2')
    cliente2 = {
        'nome': 'cliente2',
        'login': 987654321,
        'senha': 111222333,
        'data': response
    }

    usuarios_list.append(administrador)
    usuarios_list.append(cliente1)
    usuarios_list.append(cliente2)

    return usuarios_list

