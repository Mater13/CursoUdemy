#!/usr/bin/env python3
from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from orden import Orden


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', '15')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
# print(computadora1)
teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '15')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
# print(computadora2)
teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', '34')
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)
