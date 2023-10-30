# Profundizando en el tipo str

# Dar formato a un str
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
print(f'{mensaje_con_formato}\n')

# Utilizando una tupla
persona = ('Karla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' % persona
print(f'{mensaje_con_formato}\n')

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
print(f'{mensaje_con_formato}\n' % persona)

# PlaceHolder = marcador de posicion, se va a sustituir posteriormente
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}' .format(nombre, edad, sueldo)
print(f'{mensaje_con_formato}\n')

mensaje_con_formato = 'Nombre {0} Edad {1} Sueldo {2:.2f}' .format(nombre, edad, sueldo)
print(f'{mensaje_con_formato}\n')

mensaje_con_formato = 'Sueldo {2:.2f} Edad {1} Nombre {0}' .format(nombre, edad, sueldo)
print(f'{mensaje_con_formato}\n')

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}' .format(n=nombre, e=edad, s=sueldo)
print(f'{mensaje}\n')

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(f'{mensaje}\n')


# FUNCION MAS RECOMENDADA
print('Metodo Fstring'.center(50, '-'))
mensaje = f'Nombre {nombre} edad {edad} Sueldo {sueldo:.2f}'
print(f'{mensaje}\n')


# METODO PRINT
print('Metodo PRINT'.center(50, '-'))
print(nombre, edad, sueldo)  # imprime solo las variables
print(nombre, edad, sueldo, sep=', ')  # cada elemento SEParado por coma
