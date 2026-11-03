from Pokes import pokemons_db
from tree import BinaryTree
from graph import Graph
from Star_wars import personajes, episodios_compartidos
from stack import Stack

# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se 
# conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) 
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
#   a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
#   b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, 
#      es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#   c. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#   d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#   e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
#   f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#   g. determinar cuantos Pokémons tienen megaevolucion.
#   h. determinar cuantos Pokémons tiene forma gigamax.
#   i. cargue al menos 100 Pokémons.

print("================= EJERCICIO 1 =================")
print()
print()


arbol_nombre= BinaryTree()
arbol_numero= BinaryTree()
arbol_tipo= BinaryTree()

class Pokemons:
    def __init__(self, nombre, nume, tipo, debil, megaevo, giga):
        self.name= nombre
        self.num= nume
        self.type= tipo
        self.deb= debil
        self.meg= megaevo
        self.gig= giga

    def __str__(self):
        return f"Nombre: {self.name} || Número: {self.num} || Tipos: {self.type} || Debilidades: {self.deb} || Mega evolución: {self.meg} || Gigamax: {self.gig}"


# Punto A
for pokemon in pokemons_db:
    nuevo_poke= Pokemons(pokemon["nombre"], pokemon["numero"], pokemon["tipos"], pokemon["debilidades"], pokemon["mega"], pokemon["gigamax"])
    arbol_nombre.insert_node(nuevo_poke.name, nuevo_poke) # Punto A
    arbol_numero.insert_node(nuevo_poke.num, nuevo_poke) # Punto A
    arbol_tipo.insert_node(nuevo_poke.type, nuevo_poke) # Punto A

print("Punto B")
def search_numero(arbol, value): # Punto B
    
    def __search(root, value):
        aux = None
        if root is not None:
        
            if root.value == value:
                aux = root
            elif value < root.value:
                aux = __search(root.left, value)
            elif value > root.value:
                aux = __search(root.right, value)

        return aux

    node = __search(arbol.root, value)
    
    return node 

numero_de_poke= int(input("Ingrese un número de pokemon a buscar: ")) # Punto B
poke_buscado= search_numero(arbol_numero, numero_de_poke) # Punto B

if poke_buscado is not None: # Punto B
    print("El pokemon buscado es: ")
    print(poke_buscado.other_values)
else: # Punto B
    print("El número de pokemon buscado no esta en la lista.")
print()

def proxy_por_nombre(self, prefix: str): # Punto B
    encontrado= [False]    
    
    def __proxy_por_nombre(root, prefix):
        if root.left is not None:
            __proxy_por_nombre(root.left, prefix)
        if prefix.lower() in root.value.lower():
            print(root.other_values)
            encontrado[0]= True
        if root.right is not None:
            __proxy_por_nombre(root.right, prefix)

    __proxy_por_nombre(self.root, prefix)

    if not encontrado[0]:
        print("El nombre buscado no es similar a ningún otro.")

nombre_a_buscar= str(input("Ingrese el nombre del pokemon a buscar: ")) # Punto B
proxy_por_nombre(arbol_nombre, nombre_a_buscar) # Punto B
print()


print("Punto C")
def nombres_por_tipos(arbol, tipo): # Punto C

    def __nombres_por_tipos(root, type):
        if root is not None:
            if root.left is not None:
                __nombres_por_tipos(root.left, type)

            if type in root.value:
                print(root.other_values.name)

            if root.right is not None:
                __nombres_por_tipos(root.right, type)

    __nombres_por_tipos(arbol.root, tipo)

print("Pokemones de tipo Fuego:") # Punto C
nombres_por_tipos(arbol_tipo, "Fuego")
print()
print("Pokemones de tipo Eléctrico:") # Punto C
nombres_por_tipos(arbol_tipo, "Eléctrico")
print()
print("Pokemones de tipo Acero:") # Punto C
nombres_por_tipos(arbol_tipo, "Acero")
print()
print("Pokemones de tipo Fantasma:") # Punto C
nombres_por_tipos(arbol_tipo, "Fantasma")
print()


print("Punto D")
print("Listado en orden ascendete por número: ") # Punto D
arbol_numero.inorden() # Punto D
print()
print()
print("Listado en orden ascendente por nombre: ") # Punto D
arbol_nombre.inorden() # Punto D
print()
print()
print("Listado por nivel por nombre: ") # Punto D
arbol_nombre.by_level() # Punto D
print()
print()


print("Punto E")
def mostrar_debiles(arbol, tipos_atacante): # Punto E
    
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            
            pokemon = root.other_values 
            
            for tipo in tipos_atacante:
                if tipo in pokemon.deb:
                    print(pokemon)
                    break
            
            __recorrer(root.right)
            
    __recorrer(arbol.root)

existe_jolteon= arbol_nombre.search("Jolteon") # Punto E
existe_lycanroc= arbol_nombre.search("Lycanroc") # Punto E
existe_tyrantrum= arbol_nombre.search("Tyrantrum") # Punto E

if existe_jolteon: # Punto E
    print("Los pokemones que son debiles a Jolteon son: ")
    mostrar_debiles(arbol_tipo, existe_jolteon.type)
else: # Punto E
    print("Jolteon no se encuentra en la lista por lo que no se sabe su tipo y que pokemones son debiles a ellos.")

print()

if existe_lycanroc: # Punto E
    print("Los pokemones que son debiles a Lycanroc son: ")
    mostrar_debiles(arbol_tipo, existe_lycanroc.type)
else: # Punto E
    print("Lycanroc no se encuentra en la lista por lo que no se sabe su tipo y que pokemones son debiles a ellos.")

print()

if existe_tyrantrum: # Punto E
    print("Los pokemones que son debiles a Tyrantrum son: ")
    mostrar_debiles(arbol_tipo, existe_tyrantrum.type)
else: # Punto E
    print("Tyrantrum no se encuentra en la lista por lo que no se sabe su tipo y que pokemones son debiles a ellos.")
print()


print("Punto F")
def tipos_de_Pokemons(arbol): # Punto F

    conteo_tipos= {}

    def __tipos_de_pokemons(root):

        if root is not None:
            __tipos_de_pokemons(root.left)

            pokemon= root.other_values

            for tipo in pokemon.type:
                if tipo in conteo_tipos:
                    conteo_tipos[tipo]+= 1
                else:
                    conteo_tipos[tipo]= 1

            __tipos_de_pokemons(root.right)

    __tipos_de_pokemons(arbol.root)

    print("Cantidad de pokemones por tipo:")
    for tipo, cantidad in conteo_tipos.items():
        print(f"Tipo: {tipo} || Cantidad: {cantidad}")

print("Tipos de y cantidad de pokemons: ") # Punto F
tipos_de_Pokemons(arbol_tipo) # Punto F
print()


print("Punto G y H")
def contar(arbol, tranformacion): # Punto G y H

    def __contar(root):
        contador= 0

        if root is not None:
            if root.left is not None:
                contador+= __contar(root.left)

            if tranformacion.lower() == "megaevolucion":
                if root.other_values.meg:
                    contador+= 1
            elif tranformacion.lower() == "gigamax":
                if root.other_values.gig:
                    contador+= 1

            if root.right is not None:
                contador+= __contar(root.right)
        
        return contador

    count= __contar(arbol.root)

    return count

megas= contar(arbol_nombre, "megaevolucion") # Punto G
gigamax= contar(arbol_nombre, "gigamax") # Punto H

print(f"La cantidad de megaevoluciones es: {megas}") # Punto G
print(f"La cantidad de gigamax es: {gigamax}") # Punto H
print()
print()


# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para 
# resolver las siguientes tareas:
#   a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que 
#      aparecieron juntos ambos personajes que se relacionan;
#   b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
#   c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes 
#      que coinciden con dicho número;
#   d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, 
#      Chewbacca, Han Solo, R2-D2, BB-8;
#   e. calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
#   f. indicar qué personajes aparecieron en los nueve episodios de la saga.

print("================= EJERCICIO 2 =================")
print()


grafo_star_wars= Graph(is_dir= False)

# Punto A y D
for vertice in personajes: # Punto A y D
    grafo_star_wars.add_vertex(vertice)

for arista in episodios_compartidos: # Punto A
    grafo_star_wars.add_edge(arista[2], arista[0], arista[1])


print("Punto B")
lista= ["C3PO", "Yoda", "Leia"]

for personaje in lista:
    min_tree= grafo_star_wars.kruskal(personaje) # Punto B
    total_episodios= 0 # Punto B

    print(f"Árbol mínimo de {personaje}:") # Punto B
    for edge in min_tree.split(";"): # Punto B
        origen, destino, metros= edge.split("-")
        total_episodios+= int(metros)
        print(f"Origen: {origen} | Destino: {destino}.")
    print(f"El total de episodios recorridos es {total_episodios}.") # Punto B
    print()


print("Punto C")
maximo= 0 # Punto C
for vertice in grafo_star_wars: # Punto C
    for arista in vertice.edges:
        if arista.weight > maximo:
            maximo= arista.weight

print(f"Máximo de episodios compartidos: {maximo}") # Punto C
print("Pares de personajes que coinciden con dicho número:") # Punto C
for vertice in grafo_star_wars: # Punto C
    for arista in vertice.edges:
        if arista.weight == maximo and vertice.value < arista.destination:
            print(f"{vertice.value} - {arista.destination}")
print()


print("Punto E")
def camino_corto(grafo, personaje1, personaje2): # Punto E
    existe_conexion= grafo.exist_path(personaje1, personaje2)

    if existe_conexion:
        path= grafo.dijkstra(personaje1)
        destino= personaje2
        camino= []
        episodios= None

        while path.size() > 0:
            value= path.pop()
            if  value[0] == destino:
                if episodios is None:
                    episodios= value[1]
                camino.append(value[0])
                destino= value[2]
        camino.reverse()
        print(f"El camino más corto es {"-".join(camino)}; y se necesitan {episodios} episodios para conectar a {personaje1} con {personaje2}.")
    else:
        print(f"{personaje1} no se conecta con {personaje2}.")

camino_corto(grafo_star_wars, "C3PO", "R2D2") # Punto E
camino_corto(grafo_star_wars, "Yoda", "Darth Vader") # Punto E
print()


print("Punto F")
print("Los personajes que aparecieron en los nueve episodios de la saga son: ") # Punto F
for vertice in grafo_star_wars: # Punto F
    for arista in vertice.edges:
        numero_de_episodios= arista.weight
        if numero_de_episodios == 9:
            print(vertice)
            break


