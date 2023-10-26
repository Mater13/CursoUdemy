#!/usr/bin/env python3
from ManejoArchivo import ManejoArchivos

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
