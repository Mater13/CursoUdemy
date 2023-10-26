nota = int(input('Proporciones la calificacion: '))
calificacion = None
if nota <= 10 and nota >= 9:
    calificacion = 'A'
elif nota < 9 and nota >= 8:
    calificacion = 'B'
elif nota < 8 and nota >= 7:
    calificacion = 'C'
elif nota < 7 and nota >= 6:
    calificacion = 'D'
elif nota < 6 and nota >= 0:
    calificacion = 'F'
else:
    calificacion = 'Valor incorrecto'
print(f'Su nota es de: {nota} y corresponde la calificacion: {calificacion}')
