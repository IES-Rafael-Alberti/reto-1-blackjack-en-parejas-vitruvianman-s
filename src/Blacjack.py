from twoplayers import match_twoplayers
from oneplayer import match_1player
from game import clean_terminal

def modo_juego():
    
    election = None

    while election != 1 and election != 2:
        user_input = input('\n1. Dos jugadores\n2. Un jugador contra la máquina\n-> ')

        if user_input.isnumeric():
            election = int(user_input)
        if election != 1 and election != 2:
            print("Por favor, ingresa una opción válida (1 o 2).")
        else:
            print("Por favor, ingresa una opción válida (1 o 2).")

    clean_terminal()

    return election
"""
Esta función permite elegir el modo de juego. Tiene un bucle while e ifs para controlar los errores.
Cuando sea válido, retornara el valor
"""

def main():

    election = modo_juego()

    if election == 1:
        
        match_twoplayers()
   
    else:
        match_1player()

"""
Si introduciste 1, llamara al main del archivo twoplayers.py
Si introduciste 2, llamara al main del archivo oneplayer.py

"""


if __name__ == "__main__":
    main()