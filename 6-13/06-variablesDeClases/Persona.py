class Persona:
    contador_persona = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        # Persona.contador_persona += 1
        # self.id_persona = Persona.contador_persona
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('juan', 28)
print(persona1)
persona2 = Persona('karla', 30)
print(persona2)
persona3 = Persona('Eduardo', 25)
print(persona3)
# puedo incrimentar el contador, sin generar un nuevo objeto
Persona.generar_siguiente_valor()
persona4 = Persona('Maria', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_persona}')
