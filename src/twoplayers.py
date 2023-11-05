
from game import player, deal, total_value, turn, cases, clean_terminal


def match_twoplayers():

    player1 = player()
    player2 = player()
    # Se define el nombre de ambos

    player1_hand = deal()
    player2_hand = deal()
    # Se les asigna una mano inicial a cada uno

    total_player1 = total_value(player1_hand)
    total_player2 = total_value(player2_hand)
    #Se calcula el valor de su mano

    turn_counter = 1

    clean_terminal()

    stand_player1 = False
    stand_player2 = False
    # stand_player es una variable que se utiliza para saber si un jugador se ha plantado o no

    pifiada = True
    #pifiada es una variable de control de flujo para que cuando el total del jugador 1 sea superior a 21, se salga del bucle automaticamente

    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_player2 <= 21) and pifiada == True:
    #mientras que stand_player 1 y 2 no sean los dos distintos, se contniua ejecutando el programa
    #mientras que una mano no supere una mano de valor 21, se sigue ejecutando

        clean_terminal()

        print(f'Ronda {turn_counter}')
        print(f'J1 - {player1} - {player1_hand} ({total_player1})')
        print(f'J2 - {player2} - {player2_hand} ({total_player2})') 

        if not stand_player1: #si el jugador no se ha plantado, ejecuta la funcion turn()
            result_player1 = turn(player1_hand, player1)
            if result_player1 == 'plantarse':
                stand_player1 = True
            else: #sino se cambiara la mano y valor antiguo por los nuevos
                player1_hand = result_player1
                total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            pifiada = False

        elif not stand_player2:
            result_player2 = turn(player2_hand,player2)
            if result_player2 == 'plantarse':
                stand_player2 = True
            else:
                player2_hand = result_player2
                total_player2 = total_value(player2_hand)

        turn_counter += 1

    print(cases(player1_hand, player2_hand, player1, player2, total_player1, total_player2, turn_counter)) #imprimir el caso que ha ocurrido
