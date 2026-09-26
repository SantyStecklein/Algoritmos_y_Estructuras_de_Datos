from list_ import List
from Superheroes import superheroes
from entrenadores_Pokemon import entrenadores

# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic 
# a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las 
# siguientes actividades:
#   a. eliminar el nodo que contiene la información de Linterna Verde;
#   b. mostrar el año de aparición de Wolverine;
#   c. cambiar la casa de Dr. Strange a Marvel;
#   d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#      “traje” o “armadura”;
#   e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#      sea anterior a 1963;
#   f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#   g. mostrar toda la información de Flash y Star-Lord;
#   h. listar los superhéroes que comienzan con la letra B, M y S;
#   i. determinar cuántos superhéroes hay de cada casa de comic.

# heroes= List()

# class Superheroe:
#     def __init__(self, nombre, anio, comic, biografia):
#         self.name= nombre
#         self.year= anio
#         self.com= comic
#         self.bio= biografia

#     def __str__(self):
#         return f"Nombre: {self.name} || Año: {self.year} || Casa de Comic: {self.com} || Biografía: {self.bio}"

# for heroe in superheroes:
#     heroes.append(Superheroe(heroe["nombre"], heroe["año_aparicion"], heroe["casa_comic"], heroe["biografia"]))

# def by_name(item):
#     return item.name

# def by_year(item):
#     return item.year

# heroes.add_criterion("nombre", by_name)
# heroes.add_criterion("anio", by_year)


# def delete_Green_Lantern(lista: List) -> List: # Punto A
    
#     buscado= "Linterna Verde"
#     lista.delete_value(buscado, "nombre")

#     return lista


# heroes.sort_by_criterion("nombre") # Punto A
# heroes.show() # Punto A
# print()
# print(heroes.search("Linterna Verde", "nombre")) # Punto A
# print()
# sin_Green_Lantern: List # Punto A
# sin_Green_Lantern= delete_Green_Lantern(heroes) # Punto A
# sin_Green_Lantern.show() # Punto A


# def anio_Wolverine(lista: List) -> int: # Punto B

#     buscado= "Wolverine"
#     pos= lista.search(buscado, "nombre")
    
#     return lista[pos].year

# heroes.sort_by_criterion("nombre") # Punto B
# heroes.show() # Punto B
# print()
# anio= anio_Wolverine(heroes) # Punto B
# print(f"El año de aparición de Wolverine es: {anio}") # Punto B


# def change_house(lista: List) -> List: # Punto C
    
#     buscado= "Dr. Strange"
#     pos= lista.search(buscado, "nombre")
#     lista[pos].com= "Marvel"

#     return lista

# casa_Dr_Strange: List # Punto C
# casa_Dr_Strange= change_house(heroes) # Punto C
# casa_Dr_Strange.show() # Punto C


# def name_bio(lista: List) -> List: # Punto D

#     palabras_buscadas= ["traje", "armadura"]
#     lista_aux= List()
#     heroes_filtrados= lista.filter_contain_on_bio(palabras_buscadas)

#     for heroes in heroes_filtrados:
#         lista_aux.append(heroes.name)

#     return lista_aux

# print("Heroes que en su biografía menciona la palabra “traje” o “armadura”: ") # Punto D
# traje_armadura_nombre= name_bio(heroes) # Punto D

# for i in range(traje_armadura_nombre.size()): # Punto D
#     print(f"- {traje_armadura_nombre[i]}") # Punto D


# def print_name_home(lista: List) -> List: # Punto E
#     lista_aux = List()
    
#     for i in range(lista.size()):
#         if lista[i].year < 1963:
#             lista_aux.append([lista[i].name, lista[i].com])
            
#     return lista_aux

# nombre_y_casa_1963= print_name_home(heroes) # Punto E

# print("Nombre y casa de los superhéroes cuya fecha de aparición es anterior a 1963: ") # Punto E
# for heroe in range(nombre_y_casa_1963.size()): # Punto E
#     print(f"Nombre: {nombre_y_casa_1963[heroe][0]} || Casa de Comic: {nombre_y_casa_1963[heroe][1]}")


# def casa_Cap_Marvel_Muj_Maravilla(lista: List): # Punto F

#     pos_Cap_Marvel= lista.search("Capitana Marvel", "nombre")
#     pos_Muj_Maravilla= lista.search("Mujer Maravilla", "nombre")

#     return pos_Cap_Marvel, pos_Muj_Maravilla

# heroes.sort_by_criterion("nombre") # Punto F
# casa_Cap_Marvel, casa_Muj_Maravilla= casa_Cap_Marvel_Muj_Maravilla(heroes) # Punto F

# if casa_Cap_Marvel is not None: # Punto F
#     print(f"La Casa de Comics a la que pertenece la Capitana Marvel es: {heroes[casa_Cap_Marvel].com}")
# else: # Punto F
#     print("La Capitana Marvel no se encuentra en la lista.")

# if casa_Muj_Maravilla is not None: # Punto F
#     print(f"La Casa de Comics a la que pertenece la Mujer Maravilla es: {heroes[casa_Muj_Maravilla].com}")
# else: # Punto F
#     print("La Mujer Maravilla no se encuentra en la lista.")


# def flash_star_lord(lista: List): # Punto G

#     pos_Flash= lista.search("Flash", "nombre")
#     pos_Star_Lord= lista.search("Star-Lord", "nombre")

#     return pos_Flash, pos_Star_Lord

# heroes.sort_by_criterion("nombre") # Punto G
# info_Flash, info_Star_Lord= flash_star_lord(heroes) # Punto G

# if info_Flash is not None: # Punto G
#     print("Información de Flash: ")
#     print(heroes[info_Flash])
# else:
#     print("Flash no se encuentra en la lista.")

# print()

# if info_Star_Lord is not None: # Punto G
#     print("Información de Star-Lord: ")
#     print(heroes[info_Star_Lord])
# else:
#     print("Star-Lord no se encuentra en la lista.")


# def list_B_M_S(lista: List) -> list: # Punto H

#     lista_aux= List()
#     letras= ("B", "M", "S")
#     heroes_encontrados= lista.filter_start_with(letras)

#     for i in heroes_encontrados:
#         lista_aux.append(i)

#     return lista_aux

# heroes.sort_by_criterion("nombre") # Punto H
# lista_B_M_S: List # Punto H
# lista_B_M_S= list_B_M_S(heroes) # Punto H

# print("Listado de Superheroes que comienzan con la letra B, M y S:") # Punto H

# for i in range(lista_B_M_S.size()): # Punto H
#     print(lista_B_M_S[i].name)

#   i. determinar cuántos superhéroes hay de cada casa de comic.


# def cont_casa_comic(lista: List): # Punto I

#     cont_Marvel= 0
#     cont_DC= 0

#     for hero in lista:
#         if hero.com == "Marvel":
#             cont_Marvel+= 1
#         elif hero.com == "DC":
#             cont_DC+= 1

#     return cont_Marvel, cont_DC

# contador_Marvel, contador_DC= cont_casa_comic(heroes) # Punto I

# if contador_Marvel > 0: # Punto I
#     print(f"La cantidad de Superhéroes que tiene la casa de comic de Marvel es {contador_Marvel}")
# else: # Punto I
#     print("La casa de comics de Marvel no tiene Superhéroes en la lista")

# if contador_DC > 0: # Punto I
#     print(f"La cantidad de Superhéroes que tiene la casa de comic de DC es {contador_DC}")
# else: # Punto I
#     print("La casa de comics de DC no tiene Superhéroes en la lista")


# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
# la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
#   a. obtener la cantidad de Pokémons de un determinado entrenador;
#   b. listar los entrenadores que hayan ganado más de tres torneos;
#   c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#   d. mostrar todos los datos de un entrenador y sus Pokémos;
#   e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#   f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#      (tipo y subtipo);
#   g. el promedio de nivel de los Pokémons de un determinado entrenador;
#   h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#   i. mostrar los entrenadores que tienen Pokémons repetidos;
#   j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
#      o Wingull;
#   k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#      como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#      deberán mostrar los datos de ambos;

Treiners= List()

class Entrenadores:
    def __init__(self, nombre, torneos, perdidas, ganadas, pokemons):
        self.name= nombre
        self.tournament= torneos
        self.loses= perdidas
        self.wins= ganadas
        self.pokes= pokemons

    def __str__(self):
        return f"Nombre: {self.name} || Torneos Ganados: {self.tournament} || Batallas Perdidas: {self.loses} || Batallas Ganadas: {self.wins} || Pokemons: {self.pokes}"

class Pokemons:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name= nombre
        self.level= nivel
        self.type= tipo
        self.subtype= subtipo

    def __str__(self):
        return f"Nombre: {self.name} | Nivel: {self.level} | Tipo: {self.type} | Subtipo: {self.subtype}"

    def __repr__(self):
        return self.__str__()

for treiner in entrenadores:
    lista_objetos_pokemon = List()
    
    for poke_dict in treiner["pokemons"]:
        nuevo_pokemon = Pokemons(
            poke_dict["nombre"], 
            poke_dict["nivel"], 
            poke_dict["tipo"], 
            poke_dict["subtipo"]
        )
        lista_objetos_pokemon.append(nuevo_pokemon)

    nuevo_entrenador = Entrenadores(
        treiner["nombre"], 
        treiner["torneos_ganados"], 
        treiner["batallas_perdidas"], 
        treiner["batallas_ganadas"], 
        lista_objetos_pokemon
    )
    Treiners.append(nuevo_entrenador)

def by_name(item):
    return item.name.lower()

def by_tournament(item):
    return item.tournament

Treiners.add_criterion("nombre", by_name)
Treiners.add_criterion("torneo", by_tournament)

# def obtener_pokes(lista: List): # Punto A
    
#     treiner= input(str("Ingrese un entrenador del cual quiera saber la cantidad de Pokémons: "))
#     se_encuentra_en_lista= lista.search(treiner.lower(), "nombre")

#     return se_encuentra_en_lista

# entrenador_buscado= obtener_pokes(Treiners) # Punto A

# if entrenador_buscado is not None: # Punto A
#     print(f"El entrenador {Treiners[entrenador_buscado].name} tiene {len(Treiners[entrenador_buscado].pokes)} Pokémons.")
# else: # Punto A
#     print("El entrenador buscado no se encuentra en la lista o no existe.")


# def wins_3_tournaments(lista: List) -> List: # Punto B

#     lista_aux= List()

#     for treiner in lista:
#         if treiner.tournament > 3:
#             lista_aux.append(treiner)

#     return lista_aux

# entrenadores_con_mas_de_3_torneos= wins_3_tournaments(Treiners) # Punto B

# if entrenadores_con_mas_de_3_torneos: # Punto B
#     print("Entrenadores con más de 3 torneos ganados:")
#     entrenadores_con_mas_de_3_torneos.show()
# else: # Punto B
#     print("No hay entrenadores con más de 3 torneos ganados.")


# def mas_torneos(lista: List) -> List: # Punto C

#     mayor_cantidad_torneos= 0
#     entrenador= None

#     for treiner in lista:
#         if treiner.tournament > mayor_cantidad_torneos:
#             mayor_cantidad_torneos= treiner.tournament
#             entrenador= treiner

#     return entrenador

# mayor_cantidad_torneos= mas_torneos(Treiners) # Punto C

# if mayor_cantidad_torneos is not None: # Punto C
#     print(f"El entrenador/a con mayor cantidad de torneos ganados es {mayor_cantidad_torneos.name} con una cantidad de {mayor_cantidad_torneos.tournament} torneos ganados.")
# else: # Punto C
#     print("No hay entrenadores que hayan ganado torneos en la lista.")


# def datos_treiner(lista: List) -> int: # Punto D

#     entrenador= input(str("Ingrese un entrenador el cual quiera ver la información: "))
#     encontrado= lista.search(entrenador.lower(), "nombre")

#     return encontrado

# pos_entrenador= datos_treiner(Treiners) # Punto D

# if pos_entrenador is not None: # Punto D
#     print("Información del entrenador buscado: ")
#     print(Treiners[pos_entrenador])
# else: # Punto D
#     print("El entrenador buscado no se encuentra en la lista o no existe.")


# def battle_wins(lista: List) -> List: # Punto E

#     lista_aux= List()

#     for treiner in lista:
#         total_batallas= treiner.wins + treiner.loses
#         if total_batallas > 0:
#             porcen= (treiner.wins * 100) / total_batallas
#         else:
#             porcen= 0

#         if porcen > 79:
#             lista_aux.append(treiner)

#     return lista_aux

# lista_entrenadores= battle_wins(Treiners) # Punto E

# if lista_entrenadores: # Punto E
#     print("Lista de los entrenadores cuyo porcentaje de batallas ganadas es mayor al 79%: ")
#     for entrenador in lista_entrenadores:
#         print(entrenador.name)
# else: # Punto E
#     print("No hay entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79% en la lista")


# def fuego_planta_o_agua_volador(lista: List) -> List: # Punto F

#     lista_aux= List()

#     for treiner in lista:
#         for pokes in treiner.pokes:
#             if [pokes.type, pokes.subtype] == ["Fuego", "Planta"]:
#                 lista_aux.append(treiner)
#                 break
#             elif [pokes.type, pokes.subtype] == ["Agua", "Volador"]:
#                 lista_aux.append(treiner)
#                 break

#     return lista_aux

# pokes_tipos= fuego_planta_o_agua_volador(Treiners) # Punto F

# if pokes_tipos: # Punto F
#     print("Los entrenadores con Pokémons de tipo Fuego/Planta o Agua/Volador son: ")
#     for entrenador in pokes_tipos:
#         print(f"Entrenador: {entrenador.name} -- Pokémons: {entrenador.pokes}")
# else: # Punto F
#     print("No hay entrenadores con Pokémons de tipo Fuego/Planta o Agua/Volador en la lista.")


# def prom_level(lista: List, treiner: int) -> float: # Punto G

#     cantidad_pokes= 0
#     nivel_total= 0

#     for pokemon in lista[treiner].pokes:
#         nivel_total+= pokemon.level
#         cantidad_pokes+= 1

#     if cantidad_pokes > 0:
#         return nivel_total / cantidad_pokes
#     else:
#         return 0

# entrenador= input("Ingrese el entrenador el cuál desea ver el promedio de nivel de sus Pokémons: ") # Punto G
# encontrado= Treiners.search(entrenador.lower(), "nombre") # Punto G

# if encontrado is not None: # Punto G
#     promedio= prom_level(Treiners, encontrado)
#     print(f"El promedio de nivel de los Pokémons del entrenador/a {Treiners[encontrado].name} es {promedio}.")
# else: # Punto G
#     print("El entrenador no se encuentra en la lista.")


# def determinar_poke(lista: List, poke: str) -> int: # Punto H

#     cont= 0

#     for entrenador in lista:
#         esta_poke= False
        
#         for pokemon in entrenador.pokes:
#             if pokemon.name.lower() == poke.lower():
#                 esta_poke= True
#                 break

#         if esta_poke:
#             cont+= 1

#     return cont

# poke_buscado= input("Ingrese el pokemon a buscar: ") # Punto H
# cantidad_entrenadores= determinar_poke(Treiners, poke_buscado) # Punto H

# if cantidad_entrenadores > 0: # Punto H
#     print(f"La cantidad de entrenadores que tienen a {poke_buscado} es {cantidad_entrenadores}")
# else: # Punto H
#     print("No hay entrenadores que tengan a este Pokémon o el mismo no existe")


# def poke_rep(lista: List): # Punto I
#     for entrenador in lista:
#         nombres_vistos = []
        
#         for pokemon in entrenador.pokes:
#             if pokemon.name in nombres_vistos:
#                 print(entrenador.name)
#                 break
#             else:
#                 nombres_vistos.append(pokemon.name)


# print("Entrenadores con Pokémons repetidos:") # Punto I
# poke_rep(Treiners) # Punto I


# def tienen_pokes(lista: List) -> List: # Punto J

#     pokemones= ["Terrakion", "Tyrantrum", "Wingull"]
#     lista_aux= List()

#     for entrenador in lista:
#         for pokemon in entrenador.pokes:
#             if pokemon.name in pokemones:
#                 lista_aux.append(entrenador)
#                 break
    
#     return lista_aux

# entrenadores_con_pokes= tienen_pokes(Treiners) # Punto J
# entrenadores_con_pokes.show() # Punto J

#   k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#      como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#      deberán mostrar los datos de ambos;
def datos_treiner_poke(lista: List, treiner: str, pokemon: str):

    pos= lista.search(treiner.lower(), "nombre")

    if pos is None:
        return None, None
    
    lista_aux= List()
    pos_poke= 0


    if pos is not None:
        
        for poke in lista[pos].pokes:
            
            if poke.name.lower() == pokemon.lower():
                lista_aux.append(lista[pos])
                break

            pos_poke+= 1

    return lista_aux, pos_poke

entrenador= input("Ingresa el entrenador a buscar: ")
poke= input("Ingresa el Pokémon a buscar: ")
print()

datos, pos_pokes= datos_treiner_poke(Treiners, entrenador, poke)


if datos is None:
    print("El entrenador ingresado no existe en la base de datos.")
elif datos:
    for treiner in datos:
        print(f"Nombre del entrenador: {treiner.name}")
        print("Información del Pokémon: ")
        print(treiner.pokes[pos_pokes])
else:
    print(f"El entrenador {entrenador} existe, pero no tiene a {poke} en su equipo.")
