class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # sobreescribiendo en la clase padre
        return f'Persona: {self.nombre} {self.edad}'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


'''
empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
'''
