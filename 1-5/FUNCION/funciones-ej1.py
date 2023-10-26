'''
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la suma de todos los valores pasados como argumentos.
'''


def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


resul = sumar_valores(3, 5, 9, 4, 6)
print(f'El resultado de la suma es: {resul}')

print(multiplicar_valores(3, 5, 15, 3))
