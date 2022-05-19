'''
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
Criar uma função que recebe como parâmetro de entrada a lista e
uma posição (índice) dessa lista e retorna o nome que está nessa posição.
Essa função deve gerar e tratar uma exceção do tipo IndexError caso
o índice não exista na lista.
'''

def busca(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print('Erro. acesso a indice inexistente')


lista = []
for i in range(5):
    nome = input('Nome: ')
    lista.append(nome)
print(lista)

indice = int(input('Informe um índice da lista: '))
print(busca(lista, indice))
