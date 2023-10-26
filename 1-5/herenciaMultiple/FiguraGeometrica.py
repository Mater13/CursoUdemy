from abc import ABC, abstractmethod


class FiguraGeometrica:  # no es necesario indicar que deriva de la clase objet
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):  # validacion del valor asignado
            self._ancho = ancho
        else:
            self._ancho = 0
            print('Valor erroneo')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):  # sobreescribiendo en la clase padre
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto} ]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
