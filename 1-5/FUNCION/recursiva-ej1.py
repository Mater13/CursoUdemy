'''
imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
puede ser cualquier valor positivo, ejemplo, si paramos el valor de 5,
debe imprimir>
5
4
3
2
1

si se pasan valores negativos no se imprime nada
'''


def descendente(numero):
    if numero <= 0:
        return 0
    else:
        print(numero)
        return descendente(numero-1)


numero = 5
descendente(numero)


def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('valor incorrecto')


imprimir_numero_recursivo(-3)
