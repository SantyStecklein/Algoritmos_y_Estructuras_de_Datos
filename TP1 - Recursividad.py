# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
# XIV = 14, si X es mayor a I = X + (recursivo), si I es menor a V = -I + (recursivo), si V es mayor a 0 = V...

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

def convertir_num(romano: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def validar_repeticion(s):
        no_repetibles = {'V', 'L', 'D'}
        for char in no_repetibles:
            if char * 2 in s:
                return False
        for i in range(len(s) - 3):
            if s[i] == s[i+1] == s[i+2] == s[i+3]:
                return False
        return True
    
    def validar_resta(s):
        posibles_restas = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        for i in range(len(s) - 1):
            if valores[s[i]] < valores[s[i+1]]:
                if s[i] not in posibles_restas or s[i+1] not in posibles_restas[s[i]]:
                    return False
                if i > 0 and valores[s[i-1]] == valores[s[i]]:
                    return False
        return True
    
    def calcular(s):
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
    
    if not validar_repeticion(romano):
        print(f"Error:'{romano}' es invalido")
        return
    
    if not validar_resta(romano):
        print(f"Error: resta invalida en '{romano}'")
        return
    
    resultado = calcular(romano)
    print(resultado)

# ejemplos
convertir_num("II")
convertir_num("XL")
convertir_num("MDCC")
convertir_num("VVV")
convertir_num("XXXX")
convertir_num("IIX")

