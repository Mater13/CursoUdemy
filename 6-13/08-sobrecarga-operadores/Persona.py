#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 52)
print(persona1 + persona2)  # la suma contatena los nombres __add__
print(persona1 - persona2)  # la resta, resta la edad __sub__
