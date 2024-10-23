"""
    Jefe, tenemos nuevas víct... digo, visitantes. Aquí tenéis un pequeño reto para 
    que practiqueis un poquito. Tenéis que hacer un ahorcado.
    Podéis hacerlo tan complejo o simple como queráis, aquí os he dejado un trocito 
    de código para guiaros. 
    
    ¡Mucha suerte y si te surgen dudas recuerda que siempre puedes preguntar!
"""

import random


if __name__ == '__main__':

    animaciones = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']    


    palabras = open('./wordlist.txt').read().split('\n')

    def select_word():
        """
            Selecciona una palabra aleatoria de la lista de palabras
        """
        return random.choice(palabras)

    while True:

        """
            Guardamos las letras que el usuario ha introducido, aparte manejaremos todo en mayúsculas
        """

        lista_letras = []
        palabra = select_word().upper()
        palabra_oculta = ['_' for _ in palabra]
        vidas = 6

        """
            Las animaciones estan en una lista, por ello accedemos con índices,
            la palabra oculta está en forma de lista, por ello la convertimos a string para mostrarla
        """
        print(animaciones[0], '\n')
        print(' '.join(palabra_oculta), '\n')

        while True:
        

            """
                Le pedimos al usuario que introduzca una letra, si la letra ya ha sido introducida le pedimos que introduzca otra
            """
            letra = input('Introduce una letra: ').upper()
            if letra in lista_letras:
                print('Ya has introducido esta letra')
                continue

            """
                Lo guardamos en la lista de letras
            """
            lista_letras.append(letra)

            """
                Si la letra está en la palabra, recorremos la palabra con enumerate para obtener el índice y la letra
                lo mostramos en la palabra oculta, si ya no hay guiones bajos en la palabra oculta, el usuario ha ganado
            """
            if letra in palabra:
                for i, l in enumerate(palabra):
                    if l == letra:
                        palabra_oculta[i] = letra
                print(' '.join(palabra_oculta))
                if '_' not in palabra_oculta:
                    print('¡Has ganado!')
                    break

            else:
                """
                Si no estña en la palabra es que el usuario ha fallado, mostramos la animación correspondiente y restamos una vida
                cuando las vidas lleguen a 0, el usuario ha perdido
                """
                vidas -= 1
                print(animaciones[6-vidas])
                print(' '.join(palabra_oculta))
                if vidas == 0:
                    print('¡Has perdido!')
                    break

        print('-' * 40)
        """
            Preguntamos si el usuario quiere jugar otra vez, si no, salimos del bucle
        """
        if input('¿Quieres jugar otra vez? (s/n): ') != 's':
            print('=' * 40)
            break



        