class Persona0:
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28


print(type(Persona0))
persona0 = Persona0()
print(persona0.nombre)
print(persona0.apellido)
print(persona0.edad)


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Matias', 'Medina', '30')
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# modificar valores de los obejtos
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Objeto Pers 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('karla', 'Gomez', 30)
print(f'Objeto Pers 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
