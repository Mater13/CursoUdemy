# bool contiene los valores de True y False
# Tipos numericos, false para 0, true demas valores
valor = 0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 15.0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '' (cadena vacia), True demas valores
print('')
valor = ''
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas

# LISTA
print('')
valor = []
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# TUPLA
print('')
valor = ()
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = (2, 4, 5)
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# DICIONARIO
print('')
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = {'nombre': 'Juan', 'apellid': 'Perez'}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


# PARTE 2
print('')
variable = 0
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso verdadero')
else:
    print('Regreso falso')

while variable:
    print('ejecucion ciclo while')
    break
else:
    print('fin ciclo while')
