from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes
import random

# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#       a) funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#       b) funcion recursiva para listar los superheroes de la lista.

lista_ejer1= list()

for i in range(15):
    lista_ejer1.append(superheroes[random.randint(0, len(superheroes) - 1)])

def funcion_a(lista: list, posicion: int = 0) -> bool: # Punto A

    if posicion >= len(lista):
        return False
    
    value= lista[posicion]

    if value["name"] == "Captain America":
        return True
    
    return funcion_a(lista, posicion + 1)

esta_capitan_america= funcion_a(lista_ejer1)
if esta_capitan_america:
    print("El Capitan América esta en la lista.")
else:
    print("El Capitan América no esta en la lista.")
print()

def funcio_b(lista: list, posicion: int = 0) -> None:

    if posicion >= len(lista):
        return
    
    value= lista[posicion]
    print(value["name"])

    return funcio_b(lista, posicion + 1)

print("Lista de Superheroes: ")
funcio_b(lista_ejer1)
print()

# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
#       a) Listado ordenado de manera ascendente por nombre de los personajes.
#       b) Determinar en que posicion esta The Thing y Rocket Raccoon.
#       c) Listar todos los villanos de la lista.
#       d) Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#       e) Listar los superheores que comienzan con  Bl, G, My, y W.
#       f) Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#       g) Listado de superheroes ordenados por fecha de aparación.
#       h) Modificar el nombre real de Ant Man a Scott Lang.
#       i) Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#       j) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

lista_ejer2= List()

class Supers:
    def __init__(self, name, alias, realname, bio, aparicion, villano):
        self.name= name
        self.alias= alias
        self.real_name= realname
        self.bio= bio
        self.first_appearance= aparicion
        self.is_villain= villano
    
    def __str__(self):
        return f"Nombre: {self.name} | Alias: {self.alias} | Nombre real: {self.real_name} | Biografía: {self.bio} | Primera aparición: {self.first_appearance} | Es villano: {self.is_villain}"

def by_name(item): # Punto A
    return item.name

lista_ejer2.add_criterion("name", by_name) # Punto A

def by_real_name(item): # Punto F
    if item.real_name is not None:    
        return item.real_name
    else:
        return ""

lista_ejer2.add_criterion("real_name", by_real_name) # Punto F

def by_aparicion(item): # Punto G
    return item.first_appearance

lista_ejer2.add_criterion("aparicion", by_aparicion) # Punto G

for heroes in superheroes:
    lista_ejer2.append(Supers(heroes["name"], heroes["alias"], heroes["real_name"], heroes["short_bio"], heroes["first_appearance"], heroes["is_villain"]))

print("Lista ordenada por nombre (ascendente):") # Punto A
lista_ejer2.sort_by_criterion("name") # Punto A
lista_ejer2.show() # Punto A
print()

posi_The_Thing= lista_ejer2.search("The Thing", "name") # Punto B
posi_Rocket_Raccoon= lista_ejer2.search("Rocket Raccoon", "name") # Punto B

if posi_The_Thing is not None: # Punto B
    print(f"La posición en la que se encuentra The Thing es {posi_The_Thing}.")
else:
    print("The Thing no se encuentra en la lista.")

if posi_Rocket_Raccoon is not None: # Punto B
    print(f"La posición en la que se encuentra Rocket Raccoon es {posi_Rocket_Raccoon}.")
else:
    print("Rocket Raccoon no se encuentra en la lista.")
print()

def listar_villanos(lista: List) -> None: # Punto C

    hay_villanos= False

    for super in lista:

        if super.is_villain:
            hay_villanos= True
            print(super.name)
        
    if not hay_villanos:
        print("No hay villanos en la lista.")


print("Lista de villanos: ") # Punto C
listar_villanos(lista_ejer2) # Punto C
print()

def villanos_antes_1980(lista: List) -> None: # Punto D

    hay_villanos= False
    cola= Queue()

    for super in lista:

        if super.is_villain:
            hay_villanos= True
            cola.arrive(super)
        
    if not hay_villanos:
        print("No hay villanos en la lista.")
    
    if cola.size() > 0:
        while cola.size() > 0:
            value= cola.attention()
            if value.first_appearance < 1980:
                print(value.name)

print("Villanos que aparecieron por primera vez antes del 1980:") # Punto D
villanos_antes_1980(lista_ejer2) # Punto D
print()

print("Listado de heroes que comienzan con Bl, G, My, y W: ") # Punto E
lista_ejer2.filter_start_with("Bl") # Punto E
lista_ejer2.filter_start_with("G") # Punto E
lista_ejer2.filter_start_with("My") # Punto E
lista_ejer2.filter_start_with("W") # Punto E
print()

print("Lista ordenada por nombre real (ascendente):") # Punto F
lista_ejer2.sort_by_criterion("real_name") # Punto F
lista_ejer2.show() # Punto F
print()

print("Lista ordenada por fecha de aparición:") # Punto G
lista_ejer2.sort_by_criterion("aparicion") # Punto G
lista_ejer2.show() # Punto G
print()

def modificar_Ant_Man(lista: List) -> list: # Punto H

    esta_Ant_Man= False

    for super in lista:
        if super.name == "Ant Man":
            esta_Ant_Man= True
            super.real_name= "Scott Lang"

    return [lista, esta_Ant_Man]

lista_ejer2: List

lista_ejer2, esta_heroe= modificar_Ant_Man(lista_ejer2) # Punto H

if esta_heroe: # Punto H
    print("Se modifico el nombre real de Ant Man en la lista.")
    lista_ejer2.show()
else:
    print("No se encontro a Ant Man en la lista. No se hizo ningun cambio.")
print()

print("Personajes que en su biografía se incluye la palabra time-traveling o suit") # Punto I
lista_ejer2.filter_contain_on_bio(["time-traveling", "suit"]) # Punto I
print()

Electro= lista_ejer2.delete_value("Electro", "name") # Punto J
if Electro is not None: # Punto J
    print(f"""Se elimino a Electro.
Información: {Electro}""")
else:
    print("Electro no estaba en la lista.")

print()

Baron_Zemo= lista_ejer2.delete_value("Baron Zemo", "name") # Punto J
if Baron_Zemo is not None: # Punto J
    print(f"""Se elimino a Baron Zemo.
Información: {Baron_Zemo}""")
else:
    print("Baron Zemo no estaba en la lista.")
print()

print("Lista completa habiendo eliminado a Electro y Baron Zemo: ") # Punto J
lista_ejer2.show() # Punto J




