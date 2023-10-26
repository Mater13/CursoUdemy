#!/usr/bin/env python3
from NumerosIdenticosException import NumerosIdenticosException


resultado = None  # se debe declarar fuera del try/except

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('numeros identicos')
    # raise se utiliza para arrojar una EXCEPCION en cualquier parte qlo necsit
    resultado = a / b
except ZeroDivisionError as zde:
    print(f'Ocurrio un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'Ocurrio un error: {te}, {type(te)}')
except Exception as e:  # excepcion padre, o generica
    print(f'Ocurrio un error: {e}, {type(e)}')
else:  # Se va ejecutar solo si no se ejec ninguna excepcion
    print('No se arrojo ninguna Excepcion')
finally:  # Se va ejecutar siempre haya o no alguna excepcion
    print('Ejecucion del bloque Finally')


print(f'Resultado: {resultado}')
print('Continuamos...')
