from Persona import Persona

print('Creacion Objetos'.center(30, '-'))
persona1 = Persona('Karla', 'Gomez', 32)
persona1.mostrar_detalle()
print('Eliminacion Objetos'.center(30, '-'))
del persona1  # se queremos eliminar un objeto
# destructor de objetos
