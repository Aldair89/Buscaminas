import random

# Función para generar el campo minado aleatoriamente
def generar_campo_minado(filas, columnas, num_minas):
    campo_minado = [[0] * columnas for _ in range(filas)]
    minas_generadas = 0

    while minas_generadas < num_minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        if campo_minado[fila][columna] != -1:
            campo_minado[fila][columna] = -1
            minas_generadas += 1

            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < filas and 0 <= j < columnas and campo_minado[i][j] != -1:
                        campo_minado[i][j] += 1

    return campo_minado

# Función para mostrar el campo minado en la consola
def mostrar_campo_minado(campo_minado):
    filas = len(campo_minado)
    columnas = len(campo_minado[0])

    for i in range(filas):
        for j in range(columnas):
            if campo_minado[i][j] == -1:
                print("*", end=" ")
            else:
                print(campo_minado[i][j], end=" ")
        print()

# Función para jugar al Busca Minas
def jugar_busca_minas():
    filas = 10
    columnas = 10
    num_minas = 20

    campo_minado = generar_campo_minado(filas, columnas, num_minas)
    campo_visible = [[None] * columnas for _ in range(filas)]

    juego_terminado = False

    while not juego_terminado:
        mostrar_campo_minado(campo_visible)

        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))

        if campo_minado[fila][columna] == -1:
            print("¡Has encontrado una mina! ¡Juego terminado!")
            juego_terminado = True
        else:
            campo_visible[fila][columna] = campo_minado[fila][columna]

            if campo_visible == [[campo_minado[i][j] for j in range(columnas)] for i in range(filas)]:
                print("¡Felicidades! Has encontrado todas las minas. ¡Ganaste!")
                juego_terminado = True

# Jugar al Busca Minas
jugar_busca_minas()
