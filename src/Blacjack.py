from twoplayers import match_twoplayers
from oneplayer import match_1player
from game import clean_terminal

def Modo_Juego():
    
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


def main():
    election = Modo_Juego()

    if election == 1:
        
        match_twoplayers()
   
    else:
        match_1player()
        


if __name__ == "__main__":
    main()