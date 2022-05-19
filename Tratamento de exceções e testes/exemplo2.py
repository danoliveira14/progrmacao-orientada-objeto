# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.
# Solicitar os dados novamente caso o usuário informar valores inválidos


while True:
    try:
        a = int(input('Primeiro numero: '))
        b = int(input('Segundo numero: '))
        if a < 0 or b < 0:
            raise TypeError         # provoca exceção
        c = a / b
        print('Resultado: ', c)
    except TypeError:
        print('Erro. O numero informado não é positivo')
    except ValueError:
        print('Erro. O numero não é inteiro.')
    except ZeroDivisionError:
        print('Erro. Ocorreu uma divisão por zero')
    except Exception as erro:
        print('Erro inesperado.', type(erro))
    else:               # executa quando não ocorre erros
        print('Operação realizada com sucesso')
        break           # interrompe o loop


print('O programa continua executando....')