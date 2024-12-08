# Crear tablero vacío

def crear_tablero(size=10):
    return [["_" for _ in range(size)]for _ in range(size)]

# Colocar un barco en el tablero

def colocar_barco(barco, tablero):
    for fila, columna in barco:
        if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
                if tablero[fila][columna] == "-":
                    tablero[fila][columna] = "O"
                else:
                    raise ValueError(f"La posición ({fila}, {columna}) ya está ocupada.")
        else:
            raise ValueError(f"La posición ({fila}, {columna}) está fuera del tablero.")

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

# Listas de barcos

barco_1 = [(0, 1), (1, 1)] # eslora 2    
barco_2 = [(1, 3), (1, 4), (1, 5), (1, 6)]  # eslora 4
barcos = [barco_1, barco_2]

tablero = crear_tablero()

try:
    for barco in barcos: # iterar sobre los barcos y colocarlos uno por uno en el tablero
        colocar_barco(barco, tablero)
except ValueError as e:
    print(f"Error al colocar los barcos: {e}")

print("Mi Tablero")

imprimir_tablero(tablero)


# Función Disparar

def disparar(casilla, tablero):
    fila, columna = casilla
    if tablero[fila][columna] == "O":
        tablero[fila][columna] = "X" 
        print("¡Tocado!")
    elif tablero[fila][columna] == "_":
        tablero[fila][columna] = "A"
        print("¡Agua!")
    else:
        print("Ya has disparado en esta coordenada")

#Colocar barco en tablero

def colocar_barco_en_tablero(barco, tablero):
    for x, y in barco:
        tablero[x][y] = "O" 

# Función colocar_barcos: coloca los barcos de manera aleatoria en el tablero.

def colocar_barcos(tablero):

    esloras = [2, 2, 2, 3, 3, 4]
    barcos_colocados = []

    for eslora in esloras:
        barco_valido = False
        while not barco_valido:
            barco = crear_barco(eslora) # crea barco aleatorio
            if es_valida(barco, tablero): # verificar si el barco es valido
                colocar_barco_en_tablero(barco, tablero)
                barcos_colocados.append(barco)
                barco_valido = True

    return barcos_colocados   

# Función mostrar_tablero: es la encargada de imprimir el tablero en pantalla

def mostrar_tablero(tablero):
    for fila in tablero:
         print(" ".join(fila))

#Verificar ganador

def verificar_ganador(tablero):
    """Verifica si todos los barcos han sido hundidos."""
    for fila in tablero:
        if "B" in fila:
            return False
    return True

# Dinámica de turnos

# El jugador dispara contra el tablero del oponente.

def jugar_turno_jugador(PC_tablero):

    while True:
        try:
            fila = int(input("Ingresa la fila (0-3): "))
            columna = int(input("Ingresa la columna (0-3): "))
            if 0 <= fila < TABLERO_SIZE and 0 <= columna < TABLERO_SIZE:
                resultado = disparar(PC_tablero, fila, columna)
                if resultado is None:
                    print("Ya disparaste en esa posición. Intenta de nuevo.")
                else:
                    return resultado
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa números enteros.")

#La máquina dispara de forma aleatoria contra el tablero del jugador.

def jugar_turno_PC(Mi_tablero):
   
    while True:
        fila = random.randint(0, TABLERO_SIZE - 1)
        columna = random.randint(0, TABLERO_SIZE - 1)
        resultado = disparar(Mi_tablero, fila, columna)
        if resultado is not None:
            print(f"La máquina disparó en ({fila}, {columna}).")
            return resultado
        
 # Función principal para jugar.

def juego():
    print("¡Bienvenido al juego Hundir la Flota!")
    
    # Inicializar tableros
    Mi_tablero = crear_tablero()
    PC_tablero = crear_tablero()
    colocar_barcos(Mi_tablero)
    colocar_barcos(PC_tablero)
    
    print("Tu tablero:")
    mostrar_tablero(Mi_tablero, ocultar_barcos=False)

 # Ciclo del juego

while True:
        print("Tu turno:")
        mostrar_tablero(PC_tablero)
        exito = jugar_turno_jugador(PC_tablero)
        if exito:
            print("¡Le diste a un barco enemigo!")
        else:
            print("Fallaste.")

        if verificar_ganador(PC_tablero):
            print("¡Felicidades! Hundiste todos los barcos enemigos. ¡Ganaste!")
            break
        
        print("Turno de la PC:")
        exito = jugar_turno_PC(Mi_tablero)
        if exito:
            print("¡La PC acertó en tu barco!")
        else:
            print("La PC falló.")
        
        print("Tu tablero:")
        mostrar_tablero(Mi_tablero, ocultar_barcos=False)
        
        if verificar_ganador(Mi_tablero):
            print(" La PC hundió todos tus barcos. ¡Perdiste!")
            break


def jugar():
    print("¡El juego a comenzado!")

jugar()
