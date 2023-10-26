'''
Ejercicio: calculador de impuestos
crear una fn para calcular el total de un pago incluyendo un impuesto aplicado
Formula: pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuestos/100)
'''


def calculadora_impuestos(pago, interes):
    pago_total = pago + pago * (interes/100)
    return pago_total


# no olvidar que el usuario ingresa un str y debo convertir a float
pago_sin_impuestos = float(input('Proporcione el pago sin impuestos:'))
impuestos = float(input('Proporcione el monto de impuesto: '))
pago_total = calculadora_impuestos(pago_sin_impuestos, impuestos)
print(f'Pago con impuesto: {pago_total}')
