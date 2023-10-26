# CICLO FOR
cadena = 'hola'

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')

# la varible letra, se le va asignando cada caracter del string HOLA.

# palabra BREAK
for letra in 'holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break  # termina el programa, delfor no ejecuta tampoco el else del for
else:
    print('Fin del ciclo')  # no se va a imprimir por el break

# palabra CONTINUE
for i in range(6):  # range es para utilizar un rango de numeros
    if i % 2 == 0:  # si la operacion de modulo regresa cero, num PAR
        print(f'Valor: {i}')
# ahora resuelto con funcion CONTINUE de otra forma
# CONTINUE no queremos q continue con el ciclo for, vuelve a recorrerlo
for i in range(6):
    if i % 2 != 0:  # si es un numero IMPAR
        continue  # ejecuta la siguiente interacion
    print(f'Valor con continue {i}')
