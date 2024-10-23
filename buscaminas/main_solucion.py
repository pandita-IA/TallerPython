import random
import re
import time
from string import ascii_lowercase

def configurar_tablero(tamano_tablero, inicio, numero_minas):
    # Crear un tablero vacío
    tablero_vacio = [['0' for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]

    # Colocar minas en el tablero
    minas = obtener_minas(tablero_vacio, inicio, numero_minas)

    # Colocar minas en el tablero vacío
    for i, j in minas:
        tablero_vacio[i][j] = 'X'

    # Obtener números que indican la cantidad de minas alrededor
    tablero = obtener_numeros(tablero_vacio)

    return tablero, minas

def mostrar_tablero(tablero):
    tamano = len(tablero)

    horizontal = '   ' + (4 * tamano * '-') + '-'

    # Imprimir las letras de las columnas
    etiqueta_superior = '     '

    for i in ascii_lowercase[:tamano]:
        etiqueta_superior += i + '   '

    print(etiqueta_superior + '\n' + horizontal)

    # Imprimir los números de las filas
    for idx, fila in enumerate(tablero):
        fila_str = '{0:2} |'.format(idx + 1)

        for celda in fila:
            fila_str += ' ' + celda + ' |'

        print(fila_str + '\n' + horizontal)

    print('')

def obtener_celda_aleatoria(tablero):
    tamano = len(tablero)
    a = random.randint(0, tamano - 1)
    b = random.randint(0, tamano - 1)
    return a, b

def obtener_vecinos(tablero, fila, columna):
    tamano = len(tablero)
    vecinos = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (fila + i) < tamano and -1 < (columna + j) < tamano:
                vecinos.append((fila + i, columna + j))

    return vecinos

def obtener_minas(tablero, inicio, numero_minas):
    minas = []
    vecinos = obtener_vecinos(tablero, *inicio)

    for _ in range(numero_minas):
        celda = obtener_celda_aleatoria(tablero)
        # Asegurarse de que la mina no esté en la celda de inicio o en las adyacentes
        while celda == inicio or celda in minas or celda in vecinos:
            celda = obtener_celda_aleatoria(tablero)
        minas.append(celda)

    return minas

def obtener_numeros(tablero):
    for fila_idx, fila in enumerate(tablero):
        for col_idx, celda in enumerate(fila):
            if celda != 'X':  # Si no es una mina
                valores = [tablero[r][c] for r, c in obtener_vecinos(tablero, fila_idx, col_idx)]
                tablero[fila_idx][col_idx] = str(valores.count('X'))  # Contar minas

    return tablero

def mostrar_celdas(tablero, tablero_actual, fila, columna):
    # Salir si la celda ya fue mostrada
    if tablero_actual[fila][columna] != ' ':
        return

    # Mostrar la celda actual
    tablero_actual[fila][columna] = tablero[fila][columna]

    # Obtener vecinos si la celda es vacía
    if tablero[fila][columna] == '0':
        for r, c in obtener_vecinos(tablero, fila, columna):
            # Repetir para cada vecino que no tenga una bandera
            if tablero_actual[r][c] != 'F':
                mostrar_celdas(tablero, tablero_actual, r, c)

def jugar_nuevamente():
    opcion = input('¿Jugar de nuevo? (s/n): ')
    return opcion.lower() == 's'

def parsear_entrada(entrada, tamano_tablero, mensaje_ayuda):
    celda = ()
    bandera = False
    mensaje = "Celda inválida. " + mensaje_ayuda

    patron = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[tamano_tablero - 1])
    entrada_valida = re.match(patron, entrada)

    if entrada == 'ayuda':
        mensaje = mensaje_ayuda

    elif entrada_valida:
        fila = int(entrada_valida.group(2)) - 1
        columna = ascii_lowercase.index(entrada_valida.group(1))
        bandera = bool(entrada_valida.group(3))

        if -1 < fila < tamano_tablero:
            celda = (fila, columna)
            mensaje = ''

    return {'celda': celda, 'bandera': bandera, 'mensaje': mensaje}

def jugar_partida():
    tamano_tablero = 9
    numero_minas = 10

    tablero_actual = [[' ' for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]

    tablero = []
    banderas = []
    tiempo_inicio = 0

    mensaje_ayuda = ("Escribe la columna seguida de la fila (ej. a5). "
                     "Para poner o quitar una bandera, añade 'f' a la celda (ej. a5f).")

    mostrar_tablero(tablero_actual)
    print(mensaje_ayuda + " Escribe 'ayuda' para mostrar este mensaje de nuevo.\n")

    while True:
        minas_restantes = numero_minas - len(banderas)
        entrada = input('Ingresa la celda ({} minas restantes): '.format(minas_restantes))
        resultado = parsear_entrada(entrada, tamano_tablero, mensaje_ayuda + '\n')

        mensaje = resultado['mensaje']
        celda = resultado['celda']

        if celda:
            print('\n\n')
            fila, columna = celda
            celda_actual = tablero_actual[fila][columna]
            bandera = resultado['bandera']

            if not tablero:
                tablero, minas = configurar_tablero(tamano_tablero, celda, numero_minas)
            if not tiempo_inicio:
                tiempo_inicio = time.time()

            if bandera:
                # Añadir una bandera si la celda está vacía
                if celda_actual == ' ':
                    tablero_actual[fila][columna] = 'F'
                    banderas.append(celda)
                # Quitar la bandera si ya hay una
                elif celda_actual == 'F':
                    tablero_actual[fila][columna] = ' '
                    banderas.remove(celda)
                else:
                    mensaje = 'No se puede poner una bandera ahí'

            # Si hay una bandera en la celda, mostrar un mensaje
            elif celda in banderas:
                mensaje = 'Hay una bandera ahí'

            elif tablero[fila][columna] == 'X':
                print('Juego Terminado\n')
                mostrar_tablero(tablero)
                if jugar_nuevamente():
                    jugar_partida()
                return

            elif celda_actual == ' ':
                mostrar_celdas(tablero, tablero_actual, fila, columna)

            else:
                mensaje = "Esa celda ya fue mostrada"

            # Comprobar si se ha ganado
            if set(banderas) == set(minas):
                minutos, segundos = divmod(int(time.time() - tiempo_inicio), 60)
                print(
                    '¡Has ganado! '
                    'Te tomó {} minutos y {} segundos.\n'.format(minutos, segundos))
                mostrar_tablero(tablero)
                if jugar_nuevamente():
                    jugar_partida()
                return

        mostrar_tablero(tablero_actual)
        print(mensaje)

# Iniciar el juego
jugar_partida()
