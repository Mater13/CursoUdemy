# Profundizando tipo float
a = 3.0
print(f'a: {a:.2f}')
# Construtor Float puede recibir ins y str
a = float(10)
a = float('10')
print(f'a: {a:.2f}')
# Notacion exponencial (Valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')
a = 3e-5
print(f'a: {a:.5f}')
# Cualquier calculo que involucre un float, todo se convierte a float
a = 4.0 + 5
print(a)
print(type(a))
