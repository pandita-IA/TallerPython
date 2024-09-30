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


"""
    Jefe, tenemos nuevas víct... digo, visitantes. Aquí tenéis un pequeño reto para 
    que practiqueis un poquito. Tenéis que hacer un ahorcado.
    Podéis hacerlo tan complejo o simple como queráis, aquí os he dejado un trocito 
    de código para guiaros. 
    
    ¡Mucha suerte y si te surgen dudas recuerda que siempre puedes preguntar!
"""

print(animaciones[0])
palabras = open('./wordlist.txt').read().split('\n')
print(palabras)