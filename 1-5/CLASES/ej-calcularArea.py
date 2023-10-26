# se pide calcular el area de un rectangulo B x A, proporcionado por el usuario
class Area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base1 = int(input('Ingrese la base: '))
altura1 = int(input('Ingrese la altura: '))
area1 = Area(base1, altura1)
print(f'El area rectangulo{base1} * {altura1} es: {area1.calcular_area():.1f}')
