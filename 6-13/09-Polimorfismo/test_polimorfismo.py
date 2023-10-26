#!/usr/bin/env python3

from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # no es recomendable que un metodo haga muchas validaciones
    # debe ser lo mas generico posible
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):  # p/pregtar si un objto pertnece a 1 clase
        print(objeto.departamento)


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
