def sumar(a, b):  # podemos declarar valor por default para a=0 b=0
    return a + b


resultado = sumar(5, 3)
print(f'Resultado sumar: {resultado}')
# print(f'Resultado sumar: {sumar(5, 3)}')


# cuando no sabemos el largo de los parametros de la funcion se pone *
# se va generar una tupla


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')
