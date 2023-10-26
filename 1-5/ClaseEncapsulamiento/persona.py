# los metos get y set se utilizar para modificar los objetos de nuestra clase
# get=obtener/recuperar
# set=colocar/modificar


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property  # decorador para acceder al METODO, como si fuera un ATRIBUTO
    def nombre(self):
        print('llamando al metodo get nombre')
        return self._nombre

    @nombre.setter  # decorador para modificar el atributo sin el _
    def nombre(self, nombre):
        print('llamando al metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')


# metodo para evitar q esta prueba se ejecute desde otro archivo
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 33
    persona1.mostrar_detalle()
