
from game import player, deal, total_value, turn, automated_turn, cases, clean_terminal



def match_1player():
    """A game between a player and a bot

    It asks the user for a name, the cards are dealt to the user and the dealer, the value of their hand is read and they are asked if they want to hit or stand.
    As the rounds go by, they ask again if they hit or stand.
    If one of them busts or they tie return the result of the match.

    Returns:
        end_game (str): Return a string with the result of the match
    
    """
    player1 = player()
    player_crupier = 'crupier' #treats the dealer, the machine, as if it were an automated 2 player.

    player1_hand = deal()
    crupier_hand = deal()

    total_player1 = total_value(player1_hand)
    total_crupier = total_value(crupier_hand)

    turn_counter = 1
    
    stand_player1 = False
    stand_player2 = False
    pifiada = True

    clean_terminal()

    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_crupier <= 21) and pifiada == True:

        clean_terminal()

        print(f'Ronda {turn_counter}')
        print(f'J1 - {player1} - {player1_hand} ({total_player1})')
        print(f'J2 - {player_crupier} - {crupier_hand} ({total_crupier})') 

        if not stand_player1:
            result_player1 = turn(player1_hand, player1)
            if result_player1 == 'stand':
                stand_player1 = True
            else:
                player1_hand = result_player1
                total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            pifiada = False

        elif not stand_player2:
            result_player2 = automated_turn(crupier_hand, total_crupier, player_crupier) #This function is what the machine uses to play automatically
            if result_player2 == 'stand':
                stand_player2 = True
            else:
                crupier_hand = result_player2
                total_crupier = total_value(crupier_hand)

        turn_counter += 1

    end_game = cases(player1_hand, crupier_hand, player1, player_crupier, total_player1, total_crupier, turn_counter)
    
    return end_game
