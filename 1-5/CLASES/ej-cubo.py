class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def volumen_cubo(self):  #
        return self.ancho * self.profundo * self.alto


ancho = int(input('Ingrese el ancho del cubo: '))
profundo = int(input('Ingrese profundidad del cubo: '))
alto = int(input('Defina su altura: '))

cubo1 = Cubo(ancho, profundo, alto)
print(f'El volumen del cubo es : {cubo1.volumen_cubo()}')
