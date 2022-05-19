while True:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
        print('O resultado da divisão é:', z)
    except ValueError:
        print('Erro. O valor nao é inteiro')
    except ZeroDivisionError:
        print('Erro. Ocorreu uma divisão')
    else:
        print('Operação finalizada.')
        break
