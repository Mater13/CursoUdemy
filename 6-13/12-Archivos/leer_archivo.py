#!/usr/bin/env python3
archivo = open('prueba.txt', 'r', encoding='utf8')

# print(archivo.read())
# El metodo de read() lee por completo el archivo..todos los caracteres

# print(archivo.read(5))
# print(archivo.read(3))
# leemos los primeros 5 caracteres, y luego los siguientes tres

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)

# leer lineas, devuelve como una lista
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[0])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo2.write('\n')

archivo.close()
archivo2.close()
