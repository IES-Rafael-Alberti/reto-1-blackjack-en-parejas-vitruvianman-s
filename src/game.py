import random
import os

def player():

    return input('Introduce tu nombre -> ')

deck = 'A234567890JKQ'

def deal(deck):

    return deck[random.randint(0,12)] #carta aleatoria entre 1 a 13

def total_value(hand):
    total = 0
    for i in range(0,len(hand)):
        if hand[i] == 'J' or hand[i] == 'Q' or hand[i] == '0' or hand[i] == 'K':
            total += 10

        elif hand[i] == 'A':
            if total >= 11:
                total += 1
            else:
                total += 11
    
        elif hand[i].isdigit():
            total += int(hand[i])

    return total

def cases(hand1, hand2,player1, player2, total1, total2, turn_counter):

    if total1 > 21 and total2 > 21:
        return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' + 
                'Game over.¡Los dos la habeis pifiado!\n' + 
                f'J1 - {player1} - {hand1} ({total1})\n' + 
                f'J2 - {player2} - {hand2} ({total2})')

    if total1 == total2:
        return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' +
                 '¡EMPATE!\n' + f'J1 - {player1} - {hand1} ({total1})\n' 
                 + f'J2 - {player2} - {hand2} ({total2})')
    
    if total1 > total2:
        return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' + 
                f'¡Gana J2 - {player2}!\n' + 
                f'J1 - {player1} - {hand1} ({total1})\n' +
                f'J2 - {player2} - {hand2} ({total2})')

    if total2 > total1:
        return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' + 
                f'¡Gana J1 - {player1}!\n' + 
                f'J1 - {player1} - {hand1} ({total1})\n' + 
                f'J2 - {player2} - {hand2} ({total2})')
    


def turn(hand1,total1,player1):

    selection_player = None

    
    while selection_player != 1 or selection_player is None:
        
        print(f'\nTurno de {player1}')
        selection_player = int(input('1.Plantarse \n2.Pedir carta\n-> '))
        
        if selection_player == 1:
            return hand1
        
        
        if selection_player == 2:

            total1 = 0
            hand1 += deal(deck)
            total1 += total_value(hand1)
            
            if total1 > 21:
                return hand1
            
def clean_terminal():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def clean_and_banner(player1,player2,player1_hand,player2_hand,total_player1,total_player2,turn_counter):

    clean_terminal()

    print(f'Ronda {turn_counter}')

    print(f'J1 - {player1} - {player1_hand} ({total_player1})')
    print(f'J2 - {player2} - {player2_hand} ({total_player2})') 