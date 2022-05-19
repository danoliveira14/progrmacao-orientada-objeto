from modulo import soma, media_lista

try:
    resultado = soma(10, 5)
    assert resultado == 15, 'O resultado não é 15'
    print('CORRETA')
except AssertionError as erro:
    print('ERRADA', erro)

try:
    resultado = soma(-20, -30)
    assert resultado == -50
    print('CORRETA')
except AssertionError:
    print('ERRADA')

try:
    resultado = soma(0, 0)
    assert resultado == 0
    print('CORRETA')
except AssertionError:
    print('ERRADA')

try:
    resultado = media_lista([4, 5, 6])
    assert resultado == 5
    print('CORRETA')
except AssertionError:
    print('ERRADA')