# metodo de solo lectura, omito poner el metodo set
# @nombre.setter sin esto no se podria modificar el valor del atributo
# manda error al querer modificar


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property  # decorador para acceder al METODO, como si fuera un ATRIBUTO
    def nombre(self):
        print('llamando al metodo get nombre')
        return self._nombre

    # @nombre.setter  # decorador para modificar el atributo sin el _
    # def nombre(self, nombre):
    #    print('llamando al metodo set nombre')
    #    self._nombre = nombre

    def mostrar_detalle(self):
        print(f'persona: {self._nombre} {self._apellido} {self._edad}')


persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
