print('practica1')
edad = int(input('proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    # print('La infancia es increible...')
    mensaje = 'la infancia es increible'
elif 10 <= edad < 20:
    # print('Muchos cambios y mucho estudio...')
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad < 30:
    # print('Amor y comienza el trabajo...')
    mensaje = 'Amor y comienza el trabajo'
else:
    # print('Cualquier otro valor: Etapa de vida no reconocida')'
    mensaje = 'Etapa de edad no reconocida'
print(f'Tu edad es {edad}, {mensaje}')
