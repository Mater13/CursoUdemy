class MiClase:

    variables_clase = 'Valor variable clases'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():  # no recibe ninguna referencia d nuestra clase
        print(MiClase.variables_clase)  # necs util l nomb dela clase enSiMismo

    @classmethod
    def metodo_clase(cls):  # 'cls' refiere a nuestra clase
        print(cls.variables_clase)  # si reciben valores de la clase

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        # puede acceder a la variable de clase o de instancia
        print(self.variables_clase)
        print(self.variable_instancia)


MiClase.metodo_estatico()
MiClase.metodo_clase()
# un objeto creado, puede acceder al metodo de clase y de instancia
miObjeto1 = MiClase('valor variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()


'''
print(MiClase.variables_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variables_clase)

MiClase.variables_clase2 = ' valor de variable clase 2'

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variables_clase)
print(MiClase.variables_clase2)  # No la reconoce xq se creo al vuelo
print(miClase.variables_clase2)  # pero si la puede utilizar
print(miClase2.variables_clase2)
'''
