# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
# XIV = 14, si X es mayor o igual a I = X + (recursivo), si I es menor a V = -I + (recursivo), si V es mayor o igual a 0 = V...

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def validar_repeticion(s: str) -> bool:
    no_repetibles = {'V', 'L', 'D'}
    for char in no_repetibles:
        if char * 2 in s:
            return False
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            return False
    return True

def validar_resta(s: str) -> bool:
    posibles_restas = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
    for i in range(len(s) - 1):
        if valores[s[i]] < valores[s[i+1]]:
            if s[i] not in posibles_restas or s[i+1] not in posibles_restas[s[i]]:
                return False
            if i > 0 and valores[s[i-1]] == valores[s[i]]:
                return False
    return True

def calcular(s: str) -> int: # Funcion recursiva principal.
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return valores[s[0]]
    
    valor_actual = valores[s[0]]
    valor_siguiente = valores[s[1]]
    
    if valor_actual < valor_siguiente:
        return -valor_actual + calcular(s[1:])
    else:
        return valor_actual + calcular(s[1:])

def convertir_num(romano: str):
    if not validar_repeticion(romano):
        print(f"Error: '{romano}' es invalido")
        return None
        
    if not validar_resta(romano):
        print(f"Error: resta invalida en '{romano}'")
        return None
        
    resultado = calcular(romano)
    print(resultado)
    return resultado

# Ejemplos
convertir_num("II")
convertir_num("XL")
convertir_num("MDCC")
convertir_num("VVV")
convertir_num("XXXX")
convertir_num("IIX")

# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, 
# pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al 
# Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
        # a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
        # b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
        # c. Utilizar un vector para representar la mochila.

mochila= ["Zapatilla", "Cepillo de dientes", "Celular", "Sable de luz", "Campera"] # Punto C

def usar_la_fuerza(mochila: str, cont= 0) -> str:
    
    if not mochila:
        print('No hay elementos en la mochila.')
        return None
    
    if mochila[0] != "Sable de luz": # Punta A
        objeto_extraido= mochila.pop(0)
        print(f'El elemento extraido es {objeto_extraido}')
        cont+= 1
        return usar_la_fuerza(mochila, cont)

    if mochila[0] == "Sable de luz":
        print(f'Se extrajo el Sable de luz.')
        return cont

    
resultado= usar_la_fuerza(mochila)

if resultado == 0: # Punto B
    print('El sable fue el primer objeto extraido.')
elif resultado is not None:
    print(f'Para encontrar el Sable de luz fue necesario extraer {resultado} objeto/os antes del mismo.')
else:
    print('No se encontro el Sable de luz en la mochila.')

