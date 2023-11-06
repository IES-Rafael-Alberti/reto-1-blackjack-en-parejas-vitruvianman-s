from twoplayers import match_twoplayers
from oneplayer import match_1player
from game import clean_terminal

def modo_juego(election = None):
    """To choose a game mode
    
    Ask the user to make an election between 1 and 2. The program verifies if the input
    is correct and return the value, if is not, it ask for a prompt again. 

    Args:
        election (str): The election that the player mades, default is None

    Returns:
        election (int): The election that had been controlled by the conditionals.


    """

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


def main():

    """
    Depending on the election made by the player, the program will call one of the modules from other archives.

    """

    election = modo_juego()

    if election == 1:
        
        match_twoplayers()
   
    else:
        match_1player()


if __name__ == "__main__":
    main()