# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
# vi = 6,

i = 1
v = 5
x = 10
l = 50
c = 100
d = 500
m = 1000

def convertir_num(romano: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    valor_actual = (romano[0])
    valor_siguiente = (romano[1])
    if valor_actual < valor_siguiente:
        return -valor_actual + convertir_num[1:]
    if valor_actual > valor_siguiente:
        return valor_actual + convertir_num[1:]

print(convertir_num("II"))
    