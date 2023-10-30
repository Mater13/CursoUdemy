# Profundizando en el tipo str
# import math

# Concatenacion automatica en python
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'
print(mensaje)


# uso de HELP para solicitar ayuda de una funcion
# tanto general, como algo especifico
# help(math.isnan)
# help(str.capitalize)
# help(math)
# help(str)

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
mensaje1 += 'adios'
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')


# help(str.join) Convierte una Lista a una Cadena
'''
join(self, iterable, /)
    Concatenate any number of strings.

    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.

    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
'''
tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'Apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')  # .center(80, '-'))
print(f'llaves: {valores}, type: {type(valores)}')


# help(str.split) convierte una cadena a una Lista
'''
split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.
'''
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista cursos: {lista_cursos}, type: {type(lista_cursos)}')

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
print(f'Lista cursos: {lista_cursos}, type: {type(lista_cursos)}')
print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 3)
print(f'Lista cursos: {lista_cursos}, type: {type(lista_cursos)}')
print(len(lista_cursos))
