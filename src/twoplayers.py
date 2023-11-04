
from game import player, deal, total_value, turn, cases, clean_terminal, clean_and_banner

deck = 'A234567890JKQ'

def match_twoplayers():

    player1 = player()
    player2 = player()

    player1_hand = deal(deck)
    player2_hand = deal(deck)

    total_player1 = total_value(player1_hand)
    total_player2 = total_value(player2_hand)

    turn_counter = 1

    clean_terminal()

    stand_player1 = False
    stand_player2 = False
    pifiada = True

    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_player2 <= 21) and pifiada == True:
        stand_player1 = False
        stand_player2 = False

        clean_and_banner(player1, player2, player1_hand, player2_hand, total_player1, total_player2, turn_counter)

        if not stand_player1:
            result_player1 = turn(player1_hand, total_player1, player1)
            if result_player1 == 'plantarse':
                stand_player1 = True
            else:
                player1_hand = result_player1
                total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            pifiada = False

        elif not stand_player2:
            result_player2 = turn(player2_hand, total_player2, player2)
            if result_player2 == 'plantarse':
                stand_player2 = True
            else:
                player2_hand = result_player2
                total_player2 = total_value(player2_hand)

        turn_counter += 1

    print(cases(player1_hand, player2_hand, player1, player2, total_player1, total_player2, turn_counter))
