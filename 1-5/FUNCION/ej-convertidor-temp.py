'''
Ejercicio: convertidor de temperatura
realizar dos funciones para convertir de grados celsius a fahrenheit y vicevers
'''


def convertidor_FaC(temperatura):
    temperatura_C = (temperatura - 32) / 1.8
    return temperatura_C


def convertidor_CaF(temperatura):
    temperatura_F = temperatura * 1.8 + 32
    return temperatura_F


fahrenheit = float(input('ingrese la temperatura en Fahrenheit a convertir: '))
# puedo llamar a la funcion directamente en el print
print(f'F: {fahrenheit} en celsius es: {convertidor_FaC(fahrenheit):.2f}')
# si termino :.2f imprimo con 2 valores decimales nomas

celsius = float(input('Ingrese la temperatura en Celsius a convertir: '))
# o primero asignarle una variable a la funcion, luego imprimir
tempC = convertidor_CaF(celsius)
print(f'La temperatura {celsius} en Fahrenheit es: {tempC:.2f}')
