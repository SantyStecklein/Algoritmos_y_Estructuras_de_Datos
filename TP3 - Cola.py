from queue_ import Queue
from stack import Stack

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
#   a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#   b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#      la palabra ‘Python’, sin perder datos en la cola;
#   c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#      11:43 y las 15:57, y determinar cuántas son.

cola_notificaciones = Queue()

notificaciones = [
    {'hora': '09:15', 'aplicacion': 'Instagram', 'mensaje': 'A Juan le gustó tu historia.'},
    {'hora': '10:30', 'aplicacion': 'Facebook', 'mensaje': 'Tienes una nueva sugerencia de amistad.'},
    {'hora': '11:45', 'aplicacion': 'Twitter', 'mensaje': 'Un nuevo tutorial para aprender Python desde cero.'},
    {'hora': '12:10', 'aplicacion': 'WhatsApp', 'mensaje': 'Mensaje del grupo de Algoritmos.'},
    {'hora': '13:05', 'aplicacion': 'Facebook', 'mensaje': 'María comentó tu estado.'},
    {'hora': '14:20', 'aplicacion': 'Twitter', 'mensaje': 'Mirá este hilo sobre estructuras de datos.'},
    {'hora': '15:30', 'aplicacion': 'Twitter', 'mensaje': 'Optimizando código en Python para el trabajo práctico.'},
    {'hora': '15:50', 'aplicacion': 'LinkedIn', 'mensaje': 'Apareciste en 3 búsquedas esta semana.'},
    {'hora': '16:05', 'aplicacion': 'Facebook', 'mensaje': 'Recuerdo de hace 3 años.'},
    {'hora': '18:40', 'aplicacion': 'Twitter', 'mensaje': 'Cómo implementar una queue en Python fácilmente.'},
    {'hora': '20:00', 'aplicacion': 'TikTok', 'mensaje': 'Nuevos videos de tus creadores favoritos.'}
]

for noti in notificaciones:
    cola_notificaciones.arrive(noti)


def elim_face(queue: Queue) -> Queue: # Punto A
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["aplicacion"] == "Facebook":
            queue.attention()
        else:
            queue.move_to_end()
    
    return queue

def mostrar_twitter(queue: Queue) -> Queue: # Punto B
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["aplicacion"] == "Twitter" and "Python" in value["mensaje"]:
            print(value)

        queue.move_to_end()
    
    return queue

def noti_temporanea(queue: Queue) -> list: # Punto C
    pila_temp= Stack()
    tamanio_queue= queue.size()
    cont= 0

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["hora"] >= "11:43" and value["hora"] <= "15:57":
            pila_temp.push(value)
            cont+= 1

        queue.move_to_end()
    
    return [pila_temp, cont]


print("EJERCICIO 10")
print()
print()

print("Cola de Notificaciones: ")
cola_notificaciones.show()
print()

print("Punto B:")
print("Notificaciones de Twitter con la palabra 'Python' incluida en el mensaje: ")
mostrar_twitter(cola_notificaciones)
print()
print("Demostración de que no se perdieron datos en la Cola: ")
cola_notificaciones.show()
print()

print("Punto C: ")
pila: Stack
pila, contador= noti_temporanea(cola_notificaciones)
print("Notificaciones producidas entre las 11:43 y las 15:57: ")
pila.show()
print()
print(f"El numero de notificaciones es: {contador}")
print()

print("Punto A: ")
print("Cola habiendo eliminado las notificaciones de Facebook: ")
elim_face(cola_notificaciones)
cola_notificaciones.show()
print()
print()
print()


# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#   a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#   b. mostrar los nombre de los superhéroes femeninos;
#   c. mostrar los nombres de los personajes masculinos;
#   d. determinar el nombre del superhéroe del personaje Scott Lang;
#   e. mostrar todos los datos de los superhéroes o personaje cuyos nombres comienzan
#      con la letra S;
#   f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#      de superhéroes.

cola_mcu = Queue()

personajes_mcu = [
    {'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'},
    {'personaje': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'},
    {'personaje': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'},
    {'personaje': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'},
    {'personaje': 'Thor Odinson', 'superheroe': 'Thor', 'genero': 'M'},
    {'personaje': 'Hope van Dyne', 'superheroe': 'Wasp', 'genero': 'F'},
    {'personaje': 'Sam Wilson', 'superheroe': 'Falcon', 'genero': 'M'}
]

for p in personajes_mcu:
    cola_mcu.arrive(p)


def cap_marvel(queue: Queue) -> Queue: # Punto A
    tamanio_queue= queue.size()
    esta_cap= False
    nombre_cap= ""

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["superheroe"] == "Capitana Marvel":
            esta_cap= True
            nombre_cap= value["personaje"]
        
        queue.move_to_end()
    
    if esta_cap:
        print(f"El nombre de civil de la Capitana Marvel es {nombre_cap}")
    else:
        print("No se puede determinar el nombre de civil de la Capitana Marvel ya que no se encuentra en la cola")

    return queue

def supers_fem(queue: Queue) -> Queue: # Punto B
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["genero"] == "F":
            print(f"El nombre de la Superheroína es '{value["superheroe"]}'")
        
        queue.move_to_end()
    
    return queue

def supers_masc(queue: Queue) -> Queue: # Punto C
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["genero"] == "M":
            print(f"El nombre del personaje es '{value["personaje"]}'")
        
        queue.move_to_end()
    
    return queue

def scott_lang(queue: Queue) -> Queue: # Punto D
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["personaje"] == "Scott Lang":
            print(f"El nombre de superhéroe de Scott Lang es {value["superheroe"]}")
        
        queue.move_to_end()
    
    return queue

def personajes_s(queue: Queue) -> Queue: # Punto E
    tamanio_queue= queue.size()

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["personaje"][0] == "S" or value["superheroe"][0] == "S":
            print(value)
        
        queue.move_to_end()
    
    return queue

def esta_carol(queue: Queue) -> Queue: # Punto F
    tamanio_queue= queue.size()
    carol_esta= False
    nombre_carol= ""

    for i in range(tamanio_queue):
        value= queue.on_front()

        if value["personaje"] == "Carol Danvers":
            carol_esta= True
            nombre_carol= value["superheroe"]
        
        queue.move_to_end()
    
    if carol_esta:
        print(f"Carol Danvers se encuentra en la cola y su nombre de superheroína es {nombre_carol}")
    else:
        print("Carol Danvers no se encuentra en la cola")

    return queue


print("EJERCICIO 22")
print()
print()

print("Cola de Superhéroes: ")
cola_mcu.show()
print()

print("Punto A: ")
cap_marvel(cola_mcu)
print()

print("Punto B: ")
print("Nombre de las superhéroes femeninas: ")
supers_fem(cola_mcu)
print()

print("Punto C: ")
print("Nombre de los personajes masculinos: ")
supers_masc(cola_mcu)
print()

print("Punto D: ")
scott_lang(cola_mcu)
print()

print("Punto E: ")
print("Datos de los personajes o superhéroes que alguno de sus nombres comienzan con 'S': ")
personajes_s(cola_mcu)
print()

print("Punto F: ")
esta_carol(cola_mcu)

