nombres = ['Juan', 'Carla', 'Ricardo', 'Maria']
#  imrpimir la lista de nombres
print(nombres)
#  acceder a los elementos de una lista
print(nombres[0])  # el primer elemento es el numero 0
print(nombres[1])
#  acceder a los elementos de manera INVERSA
print(nombres[-1])  # -1 es el ultimo elemento
print(nombres[-2])

print('')
#  imprimir un rango de la lista
print(nombres[0:2])  # sin incluir el indice 2
#  ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
#  desde el indice indicado hasta el final de nuestra lista
print(nombres[1:])
#  cambiar un valor
nombres[3] = 'Ivone'
print(' ')
#  iterar una lista... recorrerla
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

print(' ')
#  preguntar el largo de una lista
print(f' el largo de la lista es: {len(nombres)}')  # len= cuantos elementos
# agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
# remover el ultimo valor agregado, el ultimo de la lista
nombres.pop()
print(nombres)
# eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
# borrar la lista por completo
del nombres
# print(nombres)
