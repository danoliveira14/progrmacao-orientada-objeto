'''
Crie um dicionário para armazenar uma listagem de alunos.
Utilize como chave o RA do aluno e como valor o nome do aluno.
O RA de cada aluno deve ser composto por um número inteiro
de exatamente 7 dígitos.
Caso o RA informado não esteja no formato correto, deve ser gerada
uma exceção do tipo ValueError (utilize a instrução raise).
Caso o RA informado já exista no dicionário, deve ser gerada uma
exceção do tipo TypeError (utilize a instrução raise).
'''

alunos = {}
while True:
    try:
        ra = input('RA: ')
        if ra == '':
            break
        if len(ra) < 7:
            raise ValueError('RA tem menos que 7 caracteres')   # gera uma exceção ValueError
        if len(ra) > 7:
            raise ValueError('RA tem mais que 7 caracteres')    # gera uma exceção ValueError
        # ra = int(ra)              # converte o ra para inteiro
        if ra in alunos:
            raise TypeError         # gera uma exceção TypeError
        nome = input('Nome: ')
        alunos[ra] = nome           # insere os dados no dicionario
    except ValueError as mensagem:
        print('ERRO:', mensagem)
    except TypeError:
        print('ERRO: RA ja cadastrado')
print(alunos)
