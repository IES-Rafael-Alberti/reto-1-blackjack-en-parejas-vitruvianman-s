
from game import player, deal, total_value, turn, cases, clean_terminal


def match_twoplayers():
    """Match of blackjack between one player and other

    Ask for the players the names, deal a card and them start playing turns until
    one of them bust or tie and return the result of the match.

    Returns:
        end_game
    """

    player1 = player()
    player2 = player()
    # The name of both players is defined

    player1_hand = deal()
    player2_hand = deal()
    # SEach is assigned a starting hand.

    total_player1 = total_value(player1_hand)
    total_player2 = total_value(player2_hand)
    #The value of your hand is calculated

    turn_counter = 1

    clean_terminal()

    stand_player1 = False
    stand_player2 = False
    #stand_player is a variable to know if the player decide to stand or not
    passed_value = True
    #passed_value is a variable of flow control so when the player 1 has a value greater than 21, exit the loop in the moment

    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_player2 <= 21) and passed_value == True:
    #as long as stand_player 1 and 2 are not different, the program continues executing
    #as long as a hand does not exceed a hand of value 21, it continues to be executed

        clean_terminal()

        print(f'Ronda {turn_counter}')
        print(f'J1 - {player1} - {player1_hand} ({total_player1})')
        print(f'J2 - {player2} - {player2_hand} ({total_player2})') 

        if not stand_player1: #If the player has not stood, execute the turn() function
            result_player1 = turn(player1_hand, player1)
            if result_player1 == 'stand':
                stand_player1 = True
            else: #otherwise the old hand and value will be changed for the new ones
                player1_hand = result_player1
                total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            passed_value = False

        elif not stand_player2:
            result_player2 = turn(player2_hand,player2)
            if result_player2 == 'stand':
                stand_player2 = True
            else:
                player2_hand = result_player2
                total_player2 = total_value(player2_hand)

        turn_counter += 1
    end_game = cases(player1_hand, player2_hand, player1, player2, total_player1, total_player2, turn_counter) #print the case that has occurred
    
    return end_game
