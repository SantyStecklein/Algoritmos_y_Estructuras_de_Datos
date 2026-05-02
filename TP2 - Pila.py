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

robot= Stack()

registrar_movimientos(robot, 10, "norte")
registrar_movimientos(robot, 2, "sureste")

retorno(robot)



