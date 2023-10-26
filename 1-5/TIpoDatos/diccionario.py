# diccionario
# dict (key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
# largo
print(len(diccionario))
# acceder a un elemento key
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificando un elemento
diccionario['IDE'] = 'integrated development Environment'
print(diccionario)


# recorrer los elementos, terminos y valor, necesito usar una funcion. items
for termino, valor in diccionario.items():
    print(termino, valor)

# Para racuperar solo las llaves
for termino in diccionario.keys():
    print(termino)

# para recuperar valores asosiados a cada uno de los terminos
for valor in diccionario.values():
    print(valor)

# comprobar existencia de algun elemento
print('IDE' in diccionario)

# agregar un nuevo elemento o modificarlo
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario
