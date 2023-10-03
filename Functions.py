from faker import Faker
import random

faker = Faker('pt_BR')  # chamando a função Faker com a sigla 'pt_BR' para retornar dados em portugues


def sortearBolean():

    lista = [True, False]
    response = random.choice(lista)

    return response


def ListaPessoas(num: int = 100, sortear: bool = False):

    if sortear:
        lista_dados = []

        for i in range(num):
            dados = {
                'id': i,
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
