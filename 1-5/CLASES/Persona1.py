class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}', end=" ")
        print(f'{self.valores} {self.terminos}')


persona1 = Persona('Juan', 'Perez', 28, '3517048167', 2, 3, 4, m='manzana',
                   p='pera')
persona1.mostrar_detalle()
# tambien se puede llamar a mostrar_detalle, asi..
Persona.mostrar_detalle(persona1)
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()
