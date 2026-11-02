from graph import Graph
from math import inf

# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
#    para resolver las tareas, listadas a continuación:
#       a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor,
#          router, switch, impresora;
#       b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
#          Red Hat, Debian, Arch;
#       c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
#          Red Hat, Fedora hasta la impresora;
#       d. encontrar el árbol de expansión mínima;
#       e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
#       f. indicar desde que computadora del switch 01 es el camino más corto
#          al servidor “MongoDB”;
#       g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
#       h. debe utilizar un grafo no dirigido.

Grafo= Graph(is_dir= False) # Punto H

Grafo.add_vertex("Manjaro", "PC") # Punto A
Grafo.add_vertex("Ubuntu", "PC") # Punto A
Grafo.add_vertex("Mint", "PC") # Punto A
Grafo.add_vertex("Fedora", "PC") # Punto A
Grafo.add_vertex("Parrot", "PC") # Punto A
Grafo.add_vertex("Debian", "Notebook") # Punto A
Grafo.add_vertex("Red Hat", "Notebook") # Punto A
Grafo.add_vertex("Arch", "Notebook") # Punto A
Grafo.add_vertex("Impresora", "Impresora") # Punto A
Grafo.add_vertex("Guaraní", "Servidor") # Punto A
Grafo.add_vertex("MongoDB", "Servidor") # Punto A
Grafo.add_vertex("Switch 1", "Switch") # Punto A
Grafo.add_vertex("Switch 2", "Switch") # Punto A
Grafo.add_vertex("Router 1", "Router") # Punto A
Grafo.add_vertex("Router 2", "Router") # Punto A
Grafo.add_vertex("Router 3", "Router") # Punto A

Grafo.add_edge(17, "Switch 1", "Debian")
Grafo.add_edge(18, "Switch 1", "Ubuntu")
Grafo.add_edge(22, "Switch 1", "Impresora")
Grafo.add_edge(80, "Switch 1", "Mint")
Grafo.add_edge(29, "Switch 1", "Router 1")
Grafo.add_edge(37, "Router 2", "Router 1")
Grafo.add_edge(25, "Router 2", "Red Hat")
Grafo.add_edge(9, "Router 2", "Guaraní")
Grafo.add_edge(50, "Router 2", "Router 3")
Grafo.add_edge(43, "Router 3", "Router 1")
Grafo.add_edge(61, "Switch 2", "Router 3")
Grafo.add_edge(40, "Switch 2", "Manjaro")
Grafo.add_edge(12, "Switch 2", "Parrot")
Grafo.add_edge(5, "Switch 2", "MongoDB")
Grafo.add_edge(56, "Switch 2", "Arch")
Grafo.add_edge(3, "Switch 2", "Fedora")


print("Barrido en amplitud partiendo desde Red Hat: ") # Punto B
Grafo.amplitude_show("Red Hat")
print()
print("Barrido en amplitud partiendo desde Debian: ") # Punto B
Grafo.amplitude_show("Debian")
print()
print("Barrido en amplitud partiendo desde Arch: ") # Punto B
Grafo.amplitude_show("Arch")
print()

print("Barrido en profundidad partiendo desde Red Hat: ") # Punto B
Grafo.deep_show("Red Hat")
print()
print("Barrido en profundidad partiendo desde Debian: ") # Punto B
Grafo.deep_show("Debian")
print()
print("Barrido en profundidad partiendo desde Arch: ") # Punto B
Grafo.deep_show("Arch")


# path_Manjaro= Grafo.exist_path("Manjaro", "Impresora") # Punto C
# path_Red_Hat= Grafo.exist_path("Red Hat", "Impresora") # Punto C
# path_Fedora= Grafo.exist_path("Fedora", "Impresora") # Punto C

# if path_Manjaro: # Punto C
#     path= Grafo.dijkstra("Manjaro")
#     destination= "Impresora"
#     total_weight= None
#     camino= []

#     while path.size() > 0:
#         value= path.pop()
#         if value[0] == destination:
#             if total_weight is None:
#                 total_weight= value[1]
#             camino.append(value[0])
#             destination= value[2]
    
#     camino.reverse()
    
#     print(f"El camino mas corto desde Manjaro a la Impresora es {"-".join(camino)} y su peso total es de {total_weight}")
# else: # Punto C
#     print("Manjaro no se conecta con impresora")

# print()

# if path_Red_Hat: # Punto C
#     path= Grafo.dijkstra("Red Hat")
#     destination= "Impresora"
#     total_weight= None
#     camino= []

#     while path.size() > 0:
#         value= path.pop()
#         if value[0] == destination:
#             if total_weight is None:
#                 total_weight= value[1]
#             camino.append(value[0])
#             destination= value[2]
    
#     camino.reverse()
    
#     print(f"El camino mas corto desde Red Hat a la Impresora es {"-".join(camino)} y su peso total es de {total_weight}")
# else: # Punto C
#     print("Art Hat no se conecta con impresora")

# print()

# if path_Fedora: # Punto C
#     path= Grafo.dijkstra("Fedora")
#     destination= "Impresora"
#     total_weight= None
#     camino= []

#     while path.size() > 0:
#         value= path.pop()
#         if value[0] == destination:
#             if total_weight is None:
#                 total_weight= value[1]
#             camino.append(value[0])
#             destination= value[2]
    
#     camino.reverse()
    
#     print(f"El camino mas corto desde Fedora a la Impresora es {"-".join(camino)} y su peso total es de {total_weight}")
# else: # Punto C
#     print("Fedora no se conecta con impresora")


# min_tree= Grafo.kruskal("Manjaro") # Punto D
# total_weight= 0 # Punto D

# print(min_tree) # Punto D
# for edge in min_tree.split(";"): # Punto D
#     origin, destination, weight= edge.split("-")
#     print(f"Origen: {origin} | Destino: {destination}")
#     total_weight+= int(weight)
# print(f"El peso total del árbol de expansión mínima es {total_weight}") # Punto D


# camino_mas_corto = [inf, []] # Punto E
# pcs= [] # Punto E

# for vertex in Grafo: # Punto E
#     if vertex.other_values == "PC":
#         pcs.append(vertex.value)

# for pc in pcs: # Punto E
#     if Grafo.exist_path(pc, "Guaraní"):
#         path = Grafo.dijkstra(pc)
#         destination = "Guaraní"
#         total_weight = None
#         camino = []
        
#         while path.size() > 0:
#             value = path.pop()
#             if value[0] == destination:
#                 if total_weight is None:
#                     total_weight = value[1]
#                 camino.append(value[0])
#                 destination = value[2]
        
#         camino.reverse()
        
#         if total_weight < camino_mas_corto[0]:
#             camino_mas_corto = [total_weight, camino]
#     else:
#         print(f"{pc} no se conectó con Guaraní")

# print(f"El camino más corto es {'-'.join(camino_mas_corto[1])} y su peso total es de {camino_mas_corto[0]}") # Punto E


# camino_mas_corto = [inf, []] # Punto F
# pcs= ["Mint", "Ubuntu", "Debian"] # Punto F

# for pc in pcs: # Punto F
#     if Grafo.exist_path(pc, "MongoDB"):
#         path = Grafo.dijkstra(pc)
#         destination = "MongoDB"
#         total_weight = None
#         camino = []
        
#         while path.size() > 0:
#             value = path.pop()
#             if value[0] == destination:
#                 if total_weight is None:
#                     total_weight = value[1]
#                 camino.append(value[0])
#                 destination = value[2]
        
#         camino.reverse()
        
#         if total_weight < camino_mas_corto[0]:
#             camino_mas_corto = [total_weight, camino]
#     else:
#         print(f"{pc} no se conectó con MongoDB")

# print(f"El camino más corto es {'-'.join(camino_mas_corto[1])} y su peso total es de {camino_mas_corto[0]}") # Punto F


# Grafo.delete_edge("Impresora", "Switch 1") # Punto G
# Grafo.add_edge(22, "Impresora", "Switch 2") # Punto G

# print("Barrido en amplitud partiendo desde Red Hat: ") # Punto G
# Grafo.amplitude_show("Red Hat")
# print()
# print("Barrido en amplitud partiendo desde Debian: ") # Punto G
# Grafo.amplitude_show("Debian")
# print()
# print("Barrido en amplitud partiendo desde Arch: ") # Punto G
# Grafo.amplitude_show("Arch")
# print()

# print("Barrido en profundidad partiendo desde Red Hat: ") # Punto G
# Grafo.deep_show("Red Hat")
# print()
# print("Barrido en profundidad partiendo desde Debian: ") # Punto G
# Grafo.deep_show("Debian")
# print()
# print("Barrido en profundidad partiendo desde Arch: ") # Punto G
# Grafo.deep_show("Arch")



# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
#     tareas:
#       a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#          baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#       b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
#          es la distancia entre los ambientes, se debe cargar en metros;
#       c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#          para conectar todos los ambientes;
#       d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#          determinar cuántos metros de cable de red se necesitan para conectar el router con el
#          Smart Tv.













