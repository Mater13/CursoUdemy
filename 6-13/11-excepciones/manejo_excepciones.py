#!/usr/bin/env python3
resultado = None  # se debe declarar fuera del try/except
a = 10
b = 0
try:
    resultado = a / b
except ZeroDivisionError as zde:
    print(f'Ocurrio un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'Ocurrio un error: {te}, {type(te)}')
except Exception as e:  # excepcion padre, o generica
    print(f'Ocurrio un error: {e}, {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')
