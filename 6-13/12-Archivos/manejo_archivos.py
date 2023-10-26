#!/usr/bin/env python3
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    #  encoding='utf8'>>> indica caracteres con acento
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del Archivo')
