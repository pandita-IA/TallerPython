import random

def crear_sudoku():
    # Generar una cuadrícula de Sudoku válida
    base = 3
    lado = base * base

    # Crea una cuadrícula vacía
    sudoku = [[0] * lado for _ in range(lado)]

    # Rellena la diagonal de cuadrados 3x3
    for i in range(base):
        rellena_cuadro(sudoku, i * base, i * base)

    # Rellena las celdas restantes
    rellenar(sudoku)
    
    return sudoku

def rellena_cuadro(sudoku, fila, columna):
    numeros = list(range(1, 10))
    random.shuffle(numeros)
    
    for i in range(3):
        for j in range(3):
            sudoku[fila + i][columna + j] = numeros[i * 3 + j]

def rellenar(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                random_numbers = list(range(1, 10))
                random.shuffle(random_numbers)
                for num in random_numbers:
                    if es_valido(sudoku, i, j, num):
                        sudoku[i][j] = num
                        if rellenar(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return True

def es_valido(sudoku, fila, columna, numero):
    for i in range(9):
        if sudoku[fila][i] == numero or sudoku[i][columna] == numero:
            return False

    cuadro_fila = fila // 3 * 3
    cuadro_columna = columna // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[cuadro_fila + i][cuadro_columna + j] == numero:
                return False

    return True


def tapar_casillas(sudoku, n):
    while n > 0:
        i, j = random.randint(0, 8), random.randint(0, 8)
        if sudoku[i][j] != 0:
            sudoku[i][j] = 0
            n -= 1
    return sudoku

def resuelto(sudoku):
    return all(sudoku[i][j] != 0 for i in range(9) for j in range(9))


def print_sudoku(sudoku):
    for i, fila in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print('-' * 21)
        print(' '.join(str(num) if num != 0 else ' ' for num in fila[:3]), '|', ' '.join(str(num) if num != 0 else ' ' for num in fila[3:6]), '|', ' '.join(str(num) if num != 0 else ' ' for num in fila[6:9]))
    print('\n')

if __name__ == '__main__':
    sudoku = crear_sudoku()
    sudoku_usuario = tapar_casillas([fila.copy() for fila in sudoku], 10)

    print('Para resolver el sudoku introduce la fila y la columna en la que quieres introducir el número (0-8)', '\n')
    
    while not resuelto(sudoku_usuario):
        print_sudoku(sudoku_usuario)

        fila = int(input('Introduce la fila (0-8): '))
        columna = int(input('Introduce la columna (0-8): '))
        numero = int(input('Introduce el número (1-9): '))

        if sudoku_usuario[fila][columna] == 0:
            sudoku_usuario[fila][columna] = numero
        else:
            print('No puedes introducir un número en esta casilla')
        print('\n')
        print('-' * 20)



    print('¡Enhorabuena, has resuelto el sudoku!')
