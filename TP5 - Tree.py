from tree import BinaryTree
from Superheroes import mcu_characters
from criaturas import criaturas_mitologicas

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

# arbol= BinaryTree()

class Hero:
    def __init__(self, nombre, es_hero):
        self.name= nombre
        self.is_hero= es_hero

    def __str__(self):
        return f"Nombre: {self.name} | ¿Es Heroe?: {self.is_hero}"

# for heroes in mcu_characters: # Punto A
#     nuevo_heroe= Hero(heroes["name"], heroes["is_hero"])
#     arbol.insert_node(nuevo_heroe.name, nuevo_heroe.is_hero)

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

# nombre_actual, heroe= busqueda_proxy(arbol, "Doc") # Punto E

# if nombre_actual is not None and heroe is not None: # Punto E
#     arbol.delete_node(nombre_actual)
#     correccion_Doctor_Strange= Hero("Doctor Strange", heroe)
#     arbol.insert_node(correccion_Doctor_Strange.name, correccion_Doctor_Strange.is_hero)
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

# arbol_superheroe= BinaryTree() # Punto G
# arbol_villano= BinaryTree() # Punto G
# superheroe, villano= separar_arboles(arbol) # Punto G

# for heroe in superheroe: # Punto G
#     arbol_superheroe.insert_node(heroe)
# for vill in villano: # Punto G
#     arbol_villano.insert_node(vill)

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

# print("Barrido ordenado alfabéticamente del arbol de superheroes:") # Punto G - II
# arbol_superheroe.inorden()
# print()
# print("Barrido ordenado alfabéticamente del arbol de villanos:") # Punto G - II
# arbol_villano.inorden()


# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
#     resuelva las siguientes consultas:
#         a. listado inorden de las criaturas y quienes la derrotaron;
#         b. se debe permitir cargar una breve descripción sobre cada criatura;
#         c. mostrar toda la información de la criatura Talos;
#         d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#         e. listar las criaturas derrotadas por Heracles;
#         f. listar las criaturas que no han sido derrotadas;
#         g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#            o dios que la capturo;
#         h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#            Erimanto indicando que Heracles las atrapó;
#         i. se debe permitir búsquedas por coincidencia;
#         j. eliminar al Basilisco y a las Sirenas;
#         k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#            derroto a varias;
#         l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#         m. realizar un listado por nivel del árbol;
#         n. muestre las criaturas capturadas por Heracles.

arbol_creaturas= BinaryTree()

class Criaturas:
    def __init__(self, nom, derrotado, descripcion, capturado):
        self.name= nom
        self.lose= derrotado
        self.desc= descripcion
        self.cap= capturado # Punto G

    def __str__(self):
        return f"Nombre: {self.name} | Derrotado por: {self.lose} | Descripción: {self.desc} | Capturado por: {self.cap}" # Punto G

for creatures in criaturas_mitologicas:
    nueva_criatura= Criaturas(creatures["nombre"], creatures["derrotado_por"], creatures["descripcion"], creatures["capturada_por"]) # Punto G
    arbol_creaturas.insert_node(nueva_criatura.name, nueva_criatura)

def inorden_derrota(arbol) -> None: # Punto A

    def __inorden_derrota(root):
        if root.left is not None:
            __inorden_derrota(root.left)

        print(f"Nombre: {root.value} | Derrotado por: {root.other_values[0]}")

        if root.right is not None:
            __inorden_derrota(root.right)

    __inorden_derrota(arbol.root)

# print("Listado inorden de las criaturas y quienes la derrotaron: ") # Punto A
# inorden_derrota(arbol_creaturas) # Punto A

def cargar_desc(arbol): # Punto B

    criatura= str(input("Ingrese la criatura que desea cambiar la descripcion: "))
    creature= arbol.search(criatura)
    
    if creature is not None:
        creature.other_values.desc= input("Ingrese la descripcion para esta criatura: ")
    else:
        print("La criatura ingresada no existe o no se encuentra en el arbol.")

# cargar_desc(arbol_creaturas) # Punto B
# arbol_creaturas.inorden() # Punto B

# creature= arbol_creaturas.search("Talos") # Punto C

# if creature is not None: # Punto C
#     print(creature.other_values)
# else: # Punto C
#     print("La criatura ingresada no existe o no se encuentra en el arbol.")

def mas_derrotados(arbol) -> None: # Punto D

    conteo = {}

    def __mas_derrotados(root):
        if root is not None:
            __mas_derrotados(root.left)
            
            dios = root.other_values.lose
            if dios is not None and dios != "-":
                if dios in conteo:
                    conteo[dios] += 1
                else:
                    conteo[dios] = 1
                    
            __mas_derrotados(root.right)

    __mas_derrotados(arbol.root)

    print("Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
    for i in range(3):
        max_dios = None
        max_cantidad = -1
    
        for dios, cantidad in conteo.items():
            if cantidad > max_cantidad:
                max_cantidad = cantidad
                max_dios = dios
                
        if max_dios is not None:
            print(f"- {max_dios}: {max_cantidad}")
            del conteo[max_dios]

# mas_derrotados(arbol_creaturas) # Punto D

def derrotados_por(arbol, dios: str) -> None: # Punto E

    derrotados= []

    def __derrotados_por(root, dio):
        if root.left is not None:
            __derrotados_por(root.left, dio)

        if root.other_values.lose is not None:    
            if root.other_values.lose.upper() == dio.upper():
                derrotados.append(root.value)

        if root.right is not None:
            __derrotados_por(root.right, dio)

    __derrotados_por(arbol.root, dios)

    if len(derrotados) > 0:
        print(f"Las criaturas que derroto {dios} son:")
        for creature in derrotados:
            print(creature)
    else:
        print(f"Quien se ingreso no derroto a ninguna criatura.")

# derrotados_por(arbol_creaturas, "Heracles") # Punto E

def criaturas_no_derrotadas(arbol): # Punto F

    no_derrotados= []

    def __criaturas_no_derrotadas(root):
        if root.left is not None:
            __criaturas_no_derrotadas(root.left)

        if root.other_values.lose is None:    
            no_derrotados.append(root.value)

        if root.right is not None:
            __criaturas_no_derrotadas(root.right)

    __criaturas_no_derrotadas(arbol.root)

    if len(no_derrotados) > 0:
        print(f"Las criaturas que no fueron derrotadas son:")
        for creature in no_derrotados:
            print(creature)
    else:
        print(f"Todas las criaturas en el arbol fueron derrotadas.")

# criaturas_no_derrotadas(arbol_creaturas) # Punto F

def cargar_captura(arbol, criatura: str, capturo: str): # Punto H

    creature= arbol.search(criatura)
    
    if creature is not None:
        creature.other_values.cap= capturo
    else:
        print(f"La criatura {criatura} no existe o no se encuentra en el arbol.")

cargar_captura(arbol_creaturas, "Cerbero", "Heracles") # Punto H
cargar_captura(arbol_creaturas, "Toro de Creta", "Heracles") # Punto H
cargar_captura(arbol_creaturas, "Cierva de Cerinea", "Heracles") # Punto H
cargar_captura(arbol_creaturas, "Jabalí de Erimanto", "Heracles") # Punto H

# arbol_creaturas.inorden()

# i. se debe permitir búsquedas por coincidencia;
def busqueda_coincidencia(arbol, search: str): # Punto I
    
    datos_encontrados = []
    
    def __busqueda_coincidencia(root, sear):
        if root.left is not None:
            __busqueda_coincidencia(root.left, sear)
            
        if sear.lower() in root.value.lower():
            datos_encontrados.append((root.value, root.other_values))
            
        if root.right is not None:
            __busqueda_coincidencia(root.right, sear)

    __busqueda_coincidencia(arbol.root, search)
    
    return datos_encontrados

# buscado= busqueda_coincidencia(arbol_creaturas, "Es") # Punto I

# if len(buscado) > 0: # Punto I
#     print("Las coincidencias encontradas son:")
#     for coincidencias in buscado:
#         print(coincidencias[0])
# else: # Punto I
#     print("No se encontraron coincidencias.")

arbol_creaturas.delete_node("Basilisco") # Punto J
arbol_creaturas.delete_node("Sirenas") # Punto J
# print("Arbol habiendo eliminado a el Basilisco y las Sirenas: ") # Punto J
# arbol_creaturas.inorden() # Punto J

def cargar_derrota(arbol, criatura: str, derroto: str): # Punto K

    creature= arbol.search(criatura)
    
    if creature is not None:
        creature.other_values.lose= derroto
    else:
        print(f"La criatura {criatura} no existe o no se encuentra en el arbol.")

cargar_derrota(arbol_creaturas, "Aves del Estínfalo", "Heracles derroto a varias") # Punto K
# arbol_creaturas.inorden() # Punto K
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
def cambiar_nombre(arbol, criatura: str, nuevo_nombre: str): # Punto L

    creature= arbol.search(criatura)
    
    if creature is not None:
        objeto_criatura= creature.other_values
        objeto_criatura.name= nuevo_nombre
        arbol.delete_node(criatura)
        arbol.insert_node(nuevo_nombre, objeto_criatura)
    else:
        print(f"La criatura {criatura} no existe o no se encuentra en el arbol.")

cambiar_nombre(arbol_creaturas, "Ladón", "Dragón Ladón") # Punto L
# print("Arbol cambiando Ladón por Dragón Ladón: ")
# arbol_creaturas.inorden() # Punto L

# print("Listado del arbol por nivel: ") # Punto M
# arbol_creaturas.by_level() # Punto M
# n. muestre las criaturas capturadas por Heracles.
def capturados_por(arbol, dios: str) -> None: # Punto E

    capturados= []

    def __capturados_por(root, dio):
        if root.left is not None:
            __capturados_por(root.left, dio)

        if root.other_values.lose is not None:    
            if root.other_values.lose.upper() == dio.upper():
                capturados.append(root.value)

        if root.right is not None:
            __capturados_por(root.right, dio)

    __capturados_por(arbol.root, dios)

    if len(capturados) > 0:
        print(f"Las criaturas que capturo {dios} son:")
        for creature in capturados:
            print(creature)
    else:
        print(f"Quien se ingreso no capturo a ninguna criatura.")

capturados_por(arbol_creaturas, "heracles")



