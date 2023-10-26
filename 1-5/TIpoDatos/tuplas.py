# TUPLAS, son como listas, pero inmutables
# se distigen por ser declaran con parentecis
# y cuando es un solo elemeto, debe tener una coma al final
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
# saber el largo
print(len(frutas))
# acceder a un elemento
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])  # sin incluir el ultimo elemento

print('............')
# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')
print(' ')

# cambiar valor tupla, convertimos a lista primero
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)  # volvemos a convertir la lista en tupla
print('\n', frutas, '\n')   # '\n' salto de linea
# eliminar una tupla
del frutas


# Ejercicio, dada la siguiente tupla, 13 1 8 3 2 5 8, crear una lista que solo
#  incluya los numeros menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
