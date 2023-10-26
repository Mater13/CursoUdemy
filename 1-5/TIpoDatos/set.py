# SET no mantiene un orden, no permite elementos duplicados no es posible
# modificar los elementos, pero si se puede agragar o quitar elem

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# largo
print(len(planetas))
# revisar si un elemento esta presente
print('Marte' in planetas)  # devueve un True\False
# agregar un nuevo elemento
planetas.add('Tierra')
print(planetas)
# no se pueden duplicar elementos por mas q intente agregar de nuevo
planetas.add('Tierra')
print(planetas)
# Eliminar elementos... debe estar contenido en el SET,
# posible error si escribiese mal, Tierras x ej
planetas.remove('Tierra')
print(planetas)
# eliminar elementos sin arrojar error, sin arrojar error, aunq este mal escrit
planetas.discard('Jupiter')
print(planetas)
# limpiarlo por completo
planetas.clear()
