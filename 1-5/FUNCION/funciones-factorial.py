# FUNCIONES RECURSIVAS se vuelven a llamar, hasta el punto de ruptura21>30
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
# mati, va quedando pendiente de resolver la funcion,

def factorial(numero):
    if numero == 1:  # punto de ruptura a su re-llamado
        return 1
    else:
        return numero * factorial(numero - 1)


numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
