from tree import BinaryTree
from Superheroes import mcu_characters

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
#    (MCU), desarrollar un algoritmo que contemple lo siguiente:
#       a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
#          que indica si es un héroe o un villano, True y False respectivamente;
#       b. listar los villanos ordenados alfabéticamente;
#       c. mostrar todos los superhéroes que empiezan con C;
#       d. determinar cuántos superhéroes hay el árbol;
#       e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#          encontrarlo en el árbol y modificar su nombre;
#       f. listar los superhéroes ordenados de manera descendente;
#       g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#          los villanos, luego resolver las siguiente tareas:
#             I. determinar cuántos nodos tiene cada árbol;
#             II. realizar un barrido ordenado alfabéticamente de cada árbol.

arbol= BinaryTree()

class Hero:
    def __init__(self, nombre, es_hero):
        self.name= nombre
        self.is_hero= es_hero

    def __str__(self):
        return f"Nombre: {self.name} | ¿Es Heroe?: {self.is_hero}"

for heroes in mcu_characters: # Punto A
    nuevo_heroe= Hero(heroes["name"], heroes["is_hero"])
    arbol.insert_node(nuevo_heroe.name, nuevo_heroe.is_hero)

# arbol.preorden()

def villanos_ordenados(arbol) -> None: # Punto B
    
    def __villanos_ordenados(root):
        if root is not None:
            if root.left is not None:
                __villanos_ordenados(root.left)
                
            if root.other_values is False:
                print(root.value)
                
            if root.right is not None:
                __villanos_ordenados(root.right)

    __villanos_ordenados(arbol.root)

# villanos_ordenados(arbol) # Punto B

def super_C(arbol, pre: str) -> None: # Punto C

    def __super_C(root, prefix):
        if root.left is not None:
            __super_C(root.left, prefix)

        if root.value.upper().startswith(prefix.upper()) and root.other_values:
            print(root.value)

        if root.right is not None:
            __super_C(root.right, prefix)

    __super_C(arbol.root, pre)

# super_C(arbol, "C") # Punto C

def contar_supers(arbol) -> int: # Punto D
    
    def __contar_supers(root):
        contador = 0
        
        if root is not None:
            if root.left is not None:
                contador += __contar_supers(root.left)
                
            if root.other_values: 
                contador += 1
                
            if root.right is not None:
                contador += __contar_supers(root.right)
                
        return contador


    return __contar_supers(arbol.root)

# cantidad_de_supers= contar_supers(arbol) # Punto D
# print(f"La cantidad de superheroes que hay en el arbol es {cantidad_de_supers}") # Punto D

def busqueda_proxy(arbol, search: str): # Punto E
    
    datos_encontrados = []
    
    def __busqueda_proxy(root, sear):
        if root.left is not None:
            __busqueda_proxy(root.left, sear)
            
        if sear.lower() in root.value.lower():
            datos_encontrados.append(root.value)
            datos_encontrados.append(root.other_values)
            
        if root.right is not None:
            __busqueda_proxy(root.right, sear)

    __busqueda_proxy(arbol.root, search)
    
    if len(datos_encontrados) > 0:
        return datos_encontrados[0], datos_encontrados[1]
    
    return None, None

nombre_actual, heroe= busqueda_proxy(arbol, "Doc") # Punto E

if nombre_actual is not None and heroe is not None: # Punto E
    arbol.delete_node(nombre_actual)
    correccion_Doctor_Strange= Hero("Doctor Strange", heroe)
    arbol.insert_node(correccion_Doctor_Strange.name, correccion_Doctor_Strange.is_hero)
# arbol.preorden()

def super_descendente(arbol) -> None: # Punto F

    def __super_descendente(root):
        if root.right is not None:
            __super_descendente(root.right)

        if root.other_values:
            print(root.value)

        if root.left is not None:
            __super_descendente(root.left)

    __super_descendente(arbol.root)

# super_descendente(arbol) # Punto F

def separar_arboles(arbol): # Punto G

    lista_superheroe= []
    lista_villano= []

    def __separar_arboles(root):
        if root.left is not None:
            __separar_arboles(root.left)

        if root.other_values:
            lista_superheroe.append(root.value)
        else:
            lista_villano.append(root.value)

        if root.right is not None:
            __separar_arboles(root.right)

    __separar_arboles(arbol.root)

    return lista_superheroe, lista_villano

arbol_superheroe= BinaryTree() # Punto G
arbol_villano= BinaryTree() # Punto G
superheroe, villano= separar_arboles(arbol) # Punto G

for heroe in superheroe: # Punto G
    arbol_superheroe.insert_node(heroe)
for vill in villano: # Punto G
    arbol_villano.insert_node(vill)

def contar(arbol) -> int: # Punto G - I
    
    def __contar(root):
        contador = 0
        
        if root is not None:
            if root.left is not None:
                contador += __contar(root.left)

            contador+= 1
                
            if root.right is not None:
                contador += __contar(root.right)
                
        return contador


    return __contar(arbol.root)

# nodos_superheroe= contar(arbol_superheroe) # Punto G - I
# nodos_villano= contar(arbol_villano) # Punto G - I

# if nodos_superheroe > 0: # Punto G - I
#     print(f"La cantidad de nodos que tiene el arbol de superheroes es {nodos_superheroe}")
# else:
#     print("El arbol de superheroes no tiene nodos")
# if nodos_villano > 0: # Punto G - I
#     print(f"La cantidad de nodos que tiene el arbol de villanos es {nodos_villano}")
# else:
#     print("El arbol de villanos no tiene nodos")
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Barrido ordenado alfabéticamente del arbol de superheroes:") # Punto G - II
arbol_superheroe.inorden()
print()
print("Barrido ordenado alfabéticamente del arbol de villanos:") # Punto G - II
arbol_villano.inorden()



