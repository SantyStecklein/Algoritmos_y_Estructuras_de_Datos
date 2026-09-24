from list_ import List
from Superheroes import superheroes

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

heroes= List()

class Superheroe:
    def __init__(self, nombre, anio, comic, biografia):
        self.name= nombre
        self.year= anio
        self.com= comic
        self.bio= biografia

    def __str__(self):
        return f"Nombre: {self.name} || Año: {self.year} || Casa de Comic: {self.com} || Biografía: {self.bio}"

for heroe in superheroes:
    heroes.append(Superheroe(heroe["nombre"], heroe["año_aparicion"], heroe["casa_comic"], heroe["biografia"]))

def by_name(item):
    return item.name

def by_year(item):
    return item.year

heroes.add_criterion("nombre", by_name)
heroes.add_criterion("anio", by_year)

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
# else:
#     print("La Capitana Marvel no se encuentra en la lista.")

# if casa_Muj_Maravilla is not None: # Punto F
#     print(f"La Casa de Comics a la que pertenece la Mujer Maravilla es: {heroes[casa_Muj_Maravilla].com}")

# else:
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

# def list_B_M_S(lista= List) -> list: # Punto H

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

def cont_casa_comic(lista: List):

    cont_Marvel= 0
    cont_DC= 0

    for hero in lista:
        if hero.com == "Marvel":
            cont_Marvel+= 1
        elif hero.com == "DC":
            cont_DC+= 1

    return cont_Marvel, cont_DC

contador_Marvel, contador_DC= cont_casa_comic(heroes)

if contador_Marvel > 0:
    print(f"La cantidad de Superhéroes que tiene la casa de comic de Marvel es {contador_Marvel}")
else:
    print("La casa de comics de Marvel no tiene Superhéroes en la lista")

if contador_DC > 0:
    print(f"La cantidad de Superhéroes que tiene la casa de comic de DC es {contador_DC}")
else:
    print("La casa de comics de DC no tiene Superhéroes en la lista")
