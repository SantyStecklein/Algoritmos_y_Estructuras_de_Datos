List: # Punto C

    mayor_cantidad_torneos= 0
    entrenador= None

    for treiner in lista:
        if treiner.tournament > mayor_cantidad_torneos:
            mayor_cantidad_torneos= treiner.tournament
            entrenador= treiner

    return entrenador

mayor_cantidad_torneos= mas_torneos(Treiners) # Punto C

if mayor_cantidad_torneos is not None: # Punto C
    print(f"El entrenador/a con mayor cantidad de torneos ganados es {mayor_cantidad_torneos.name} con una cantidad de {mayor_cantidad_torneos.tournament} torneos ganados.")
else: # Punto C
    print("No hay entrenadores que hayan ganado torneos en la lista.")