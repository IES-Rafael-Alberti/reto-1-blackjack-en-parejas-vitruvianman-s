
from game import player, deal, total_value, turn, cases, clean_terminal, clean_and_banner

deck = 'A234567890JKQ'

def main():
    player1 = player()
    player2 = player()

    player1_hand = deal(deck)
    player2_hand = deal(deck)

    total_player1 = total_value(player1_hand)
    total_player2 = total_value(player2_hand)

    turn_counter = 1

    clean_terminal()

    while total_player1 <= 21 and (total_player2 <= 21 or total_player1 == total_player2):

        clean_and_banner(player1,player2,player1_hand,player2_hand,total_player1,total_player2,turn_counter)

        player1_hand = turn(player1_hand,total_player1,player1)
        total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            
            turn_counter += 1
            print(cases(player1_hand,player2_hand,player1,player2,total_player1,total_player2,turn_counter))

        else:

            clean_and_banner(player1,player2,player1_hand,player2_hand,total_player1,total_player2,turn_counter)

            player2_hand = turn(player2_hand,total_player2,player2)
            total_player2 = total_value(player2_hand)
            
            turn_counter += 1

            print(cases(player1_hand,player2_hand,player1,player2,total_player1,total_player2,turn_counter))

if __name__ == "__main__":
    main()