
from game import player, deal, total_value, turn, cases, clean_terminal, clean_and_banner

deck = 'A234567890JKQ'

def match_1player():
    player1 = player()
    player_crupier = 'crupier'

    player1_hand = deal(deck)
    crupier_hand = deal(deck)

    total_player1 = total_value(player1_hand)
    total_crupier = total_value(crupier_hand)

    turn_counter = 1
    
    stand_player1 = False
    stand_player2 = False
    pifiada = True

    clean_terminal()

    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_crupier <= 21) and pifiada == True:
        stand_player1 = False
        stand_player2 = False

        clean_and_banner(player1, player_crupier, player1_hand, crupier_hand, total_player1, total_crupier, turn_counter)

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
            result_player2 = turn(crupier_hand, total_crupier, player_crupier)
            if result_player2 == 'plantarse':
                stand_player2 = True
            else:
                crupier_hand = result_player2
                total_crupier = total_value(crupier_hand)

        turn_counter += 1

    print(cases(player1_hand, crupier_hand, player1, player_crupier, total_player1, total_crupier, turn_counter))
