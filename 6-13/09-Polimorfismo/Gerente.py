#!/usr/bin/env python3
from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Depmento: {self.departamento}] {super().__str__()}'
