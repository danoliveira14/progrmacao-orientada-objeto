# Conta todos os caracteres de uma string

def conta_vogais(texto):
    vogais = {}
    for c in texto:         # percorre os caracteres do texto
        if c in vogais:
            vogais[c] += 1
        else:
            vogais[c] = 1

    return vogais

texto = 'Exemplo de texto para testar a funcao'
print(conta_vogais(texto))




