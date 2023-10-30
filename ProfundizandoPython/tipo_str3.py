# Profundizando en el tipo str

# multiplicacion STR
resultado = 3*'Hola'
print(f'Resultado: {resultado}')

# multiplicacion tuplas
resultado = 5*('Hola', 10)
print(f'Resultado: {resultado}')

# multiplicacion Listas
resultado = 10*[0]
print(f'Resultado: {resultado} Largo: {len(resultado)}')

# caracteres de escape. diagonal inversa \
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b'  # no funciono
print(f'Resultado: {resultado}')

# caracter de diagonal inversa \
resultado = 'c:\\directorio\\juan'
print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de linea'
print(f'Resultado: {resultado}')

# Profundizando en el tipo str

# caracteres unicode
# https://symbl.cc/en/unicode/table/#basic-latin
print('Hola\u0020Mundo')
print('Notación simple:', '\u0041')
print('Notación extendida:', '\U00000041')
print('Notación hexadecimal', '\x41')
print('Corazón:', '\u2665')
print('Cara sonriendo:', '\U0001f600')
print('Serpiente:', '\U0001F40D')

# Caracteres ascii
# https://www.ascii-code.com/
caracter = chr(65)
print('A mayúscula:', caracter)
caracter = chr(64)
print('Símbolo @:', caracter)
caracter = chr(97)
print('a minúscula:', caracter)
