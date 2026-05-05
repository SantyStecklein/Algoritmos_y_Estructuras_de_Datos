from stack import Stack

# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

direccion_opuesto= {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

robot= Stack()


def registrar_movimientos(pila_historial: Stack, pasos: int, direc: str) -> None:
    
    if direc in direccion_opuesto:
        movimientos= (pasos, direc)
    else:
        print("Error: no es una direccion valida.")
        return
    
    pila_historial.push(movimientos)
    
    print(f"Se registro/registraron: {pasos} pasos en la direccion {direc}.")


def retorno(pila_historial: Stack) -> None:
    
    while pila_historial.size() > 0:
        ultimo_movimiento= pila_historial.pop()
       
        pasos= ultimo_movimiento[0]
        direccion= ultimo_movimiento[1]
        direccion_regreso= direccion_opuesto[direccion]
        
        print(f"Para volver al lugar de partida: mover {pasos} pasos en la direccion {direccion_regreso}.")


print("EJERCICIO 20:")

registrar_movimientos(robot, 10, "norte")
registrar_movimientos(robot, 2, "sureste")

print()

retorno(robot)

print()

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad 
# de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
#   a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#   b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#   c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#   d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

datos_personajes = [
    ("Iron Man", 10),
    ("Captain America", 9),
    ("Black Widow", 9),
    ("Thor", 9),
    ("Hulk", 8),
    ("Hawkeye", 5),
    ("Doctor Strange", 6),
    ("Rocket Raccoon", 6),
    ("Groot", 6),
    ("Gamora", 5),
    ("Drax", 6),
    ("Captain Marvel", 3),
    ("Ant-Man", 5),
    ("Spider-Man", 6),
    ("Winter Soldier", 7),
    ("Falcon", 6)
]

pila_mcu = Stack()

for personaje in datos_personajes:
    pila_mcu.push(personaje)


def pos_Rocket_y_Groot(pila: Stack) -> tuple: # Punto A
    pila_aux = Stack()
    
    pos_rocket = 0
    pos_groot = 0
    posicion_actual = 1
    
    while pila.size() > 0:
        nombre, peliculas = pila.pop()
        
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual
            
        pila_aux.push((nombre, peliculas))
        
        posicion_actual += 1
        
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
        
    return pos_rocket, pos_groot


def per_5_pelis(pila: Stack) -> None: # Punto B
    pila_aux= Stack()

    while pila.size() > 0:
        nombre, peliculas= pila.pop()

        if peliculas > 5:
            print(f"El personaje {nombre} tiene {peliculas} participaciones en peliculas del MCU.")

        pila_aux.push((nombre, peliculas))
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def pel_Viuda_Negra(pila: Stack) -> None: # Punto C
    pila_aux = Stack()
    
    VN_no_esta= True

    while pila.size() > 0:
        nombre, peliculas = pila.pop()
        
        if nombre == "Black Widow":
            print(f"La Viuda Negra participo en {peliculas} peliculas.")
            VN_no_esta= False

        pila_aux.push((nombre, peliculas))
        
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    if VN_no_esta:
        print("La Viuda Negra no se encuentra en la pila.")


def per_CDG(pila: Stack) -> None: # Punto D
    pila_aux= Stack()

    no_hay_per_CDG= True

    while pila.size() > 0:
        nombre, peliculas= pila.pop()

        if nombre[0] == "C" or nombre[0] == "D" or nombre[0] == "G":
            print(f"El personaje llamado/a {nombre} empieza con la letra {nombre[0]}.")
            no_hay_per_CDG= False

        pila_aux.push((nombre, peliculas))
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    if no_hay_per_CDG:
        print("No hay personajes cuyo nombre empiece con C, D o G.")


print("EJERCICIO 24:")

pos_r, pos_g= pos_Rocket_y_Groot(pila_mcu)

if pos_r != 0:
    print(f"Posicion en la que se encuentra Rocket Raccoon: {pos_r}.")
else:
    print("Rocket Raccoon no se encuentra en la pila de personajes del MCU.")
if pos_g != 0:
    print(f"Posicion en la que se encuentra Groot: {pos_g}.")
else:
    print("Groot no se encuentra en la pila de personajes del MCU.")

print()

per_5_pelis(pila_mcu)

print()

pel_Viuda_Negra(pila_mcu)

print()

per_CDG(pila_mcu)