# Manejo de valores infinitos
import math
from decimal import Decimal

# Utilizando modulo Float
print('Utilizando Modulo float')
infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Infinito positivo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')


# Utilizando el modulo de math
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Infinito positivo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Utilicando el Modulo Decimal:
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')
