'''
Escreva uma função que conta a quantidade de vogais em um texto e
armazena tal quantidade em um dicionário, onde a chave é a vogal
e o valor é a quantidade de vezes que essa vogal aparece no texto.

Exemplo:
Para o texto: "faculdade de tecnologia impacta"
A função deve retornar o dicionário: {'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}
'''

def conta_vogais(texto):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o':0, 'u':0}
    for c in texto:         # percorre os caracteres dod texto
        if c == 'a':
            vogais['a'] += 1
        elif c == 'e':
            vogais['e'] += 1
        elif c == 'i':
            vogais['i'] += 1
        elif c == 'o':
            vogais['o'] += 1
        elif c == 'u':
            vogais['u'] += 1
    return vogais

texto = 'exemplo de texto para testar a funcao'
print(conta_vogais(texto))



