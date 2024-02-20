# Juego del Cuento
import random
import time

# Definimos las variables globales
personajes = []
enemigos = []
misiones = []
mapa = {}

# Función para crear un personaje
def crear_personaje(nombre, clase, habilidades):
    personaje = {
        "nombre": nombre,
        "clase": clase,
        "habilidades": habilidades,
        "vida": 100,
        "experiencia": 0
    }
    personajes.append(personaje)

# Función para crear un enemigo
def crear_enemigo(nombre, tipo, ataque, defensa):
    enemigo = {
        "nombre": nombre,
        "tipo": tipo,
        "ataque": ataque,
        "defensa": defensa,
        "vida": 100
    }
    enemigos.append(enemigo)

# Función para crear una misión
def crear_mision(nombre, descripcion, objetivo, recompensa):
    mision = {
        "nombre": nombre,
        "descripcion": descripcion,
        "objetivo": objetivo,
        "recompensa": recompensa
    }
    misiones.append(mision)

# Función para generar el mapa
def generar_mapa():
    for i in range(10):
        for j in range(10):
            mapa[(i, j)] = " "

    # Posicionamos al jugador en el centro del mapa
    mapa[(5, 5)] = "@"

# Función para mostrar el mapa
def mostrar_mapa():
    for i in range(10):
        for j in range(10):
            print(mapa[(i, j)], end="")
        print()

# Función para mover al jugador
def mover_jugador(direccion):
    x, y = 5, 5

    if direccion == "arriba":
        y -= 1
    elif direccion == "abajo":
        y += 1
    elif direccion == "izquierda":
        x -= 1
    elif direccion == "derecha":
        x += 1

    if 0 <= x < 10 and 0 <= y < 10:
        mapa[(x, y)] = "@"
        mapa[(5, 5)] = " "

# Función para combatir contra un enemigo
def combatir(enemigo):
    while enemigo["vida"] > 0 and jugador["vida"] > 0:
        # El jugador ataca
        ataque_jugador = random.randint(1, 10) + jugador["habilidades"]["ataque"]
        enemigo["vida"] -= ataque_jugador

        # El enemigo ataca
        ataque_enemigo = random.randint(1, 10) + enemigo["ataque"]
        jugador["vida"] -= ataque_enemigo

    if jugador["vida"] > 0:
        print("¡Has derrotado al enemigo!")
        jugador["experiencia"] += enemigo["experiencia"]
    else:
        print("¡Has sido derrotado!")

# Función para iniciar el juego
def iniciar_juego():
    # Creamos al jugador
    jugador = crear_personaje("John Doe", "Hacker", {"ataque": 10, "defensa": 5})

    # Creamos un enemigo
    enemigo = crear_enemigo("Dron de seguridad", "Mecánico", 15, 10)

    # Creamos una misión
    mision = crear_mision("Infiltrar Arasaka", "Infiltrate en la sede de Arasaka y roba información confidencial", "Acceso a los servidores de Arasaka", 100)

    # Generamos el mapa
    generar_mapa()

    # Bucle principal del juego
    while True:
        # Mostramos el mapa
        mostrar_mapa()

        # Pedimos al jugador una acción
        accion = input("¿Qué quieres hacer? ")

        if accion == "mover":
            direccion = input("¿En qué dirección quieres moverte? ")
            mover_jugador(direccion)
        elif accion == "combatir":
            combatir(enemigo)
        elif accion == "salir":
            break

# Iniciamos el juego
in
