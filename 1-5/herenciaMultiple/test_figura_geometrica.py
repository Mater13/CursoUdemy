from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
print(f' Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

# MRO - Method Resolution Order
# print(Cuadrado.mro())
# sirve para saber el orden en que se van a mandar a llamar

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 8, 'Azul')
print(f' Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
