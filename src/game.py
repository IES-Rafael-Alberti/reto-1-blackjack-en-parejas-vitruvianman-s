import random
import os
import time 

def player():
    """Ask for the nickname of the player

    """

    return input('Introduce tu nombre -> ')

def deal():
    """Return one of the cards from the desk

    """
    deck = 'A234567890JKQ' 

    return deck[random.randint(0,12)] #random card between 1 and 13


def total_value(hand:str) -> int:
    """ Transform the text from the hand to numeric value 

    Get each letter in hand variable, it pass for a loop that every time check each
    letter of it, and adding the numeric equivalent of it.

    Args: 
        hand (str): The hand of the player 

    Returns: 
        total (int): The numeric value of the player hand


    """
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


def cases(hand1:str,hand2:str,player1:str,player2:str,total1:int,total2:int,turn_counter:int) -> str:
    """Possible cases of the end of the game.

    By the variables of the function, the end of the game will have
    4 different situations.

    Args:
        hand1 (str): 
            The hand of the player1.
        hand2 (str): 
            The hand of the player2.
        player1 (str): 
            Nickname of player1.
        player2 (str): 
            Nickname of player2.
        total1 (int):
            Numerical value of player 1's hand.
        total2 (int):
            Numerical value of players 2's hand.
        turn_counter(int):
            The counter of the turn of the match.

    Returns:
        Phrase (str): String with the result of the game.
        

    """
    
    if total1 > 21:
        if total2 > 21:
            result = 'Game over. ¡Los dos la habeis pifiado!'

        else:
            result = f'¡Gana J2 - {player2}!'
      
    elif total2 > 21:
        result = f'¡Gana J1 - {player1}!'
  
    else:
        difference1 = abs(21 - total1)
        difference2 = abs(21 - total2)

        if difference1 == difference2:
            result = '¡EMPATE!'

        elif difference1 < difference2:
            result = f'¡Gana J1 - {player1}!'
        else:
            result = f'¡Gana J2 - {player2}!'


    return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' +
            f'{result}\n' +
            f'J1 - {player1} - {hand1} ({total1})\n' +
            f'J2 - {player2} - {hand2} ({total2})\n')


def turn(hand:str,player:str) -> str:
    """ A turn of the blackjack game.

    The player of the turn will be asked to write a option.
    If its valid it will stand or hit another card.
    If not will ask again the player for an input.

    Args:
        hand1 (str): Hand of one of the players.
        player (str): The nickname of a player.

    Returns:

        hand (str): Hand of the player with one more card.
        stand (str): A string that will be treated later.
    """

    selection_player = None
    
    while selection_player != 1 or selection_player != 2 or selection_player is None:
        
        print(f'\nTurno de {player}')
        selection_player = input('1.Plantarse \n2.Pedir carta\n-> ')
        if selection_player.isnumeric():
            selection_player = int(selection_player)

        else:
            print('---Introduce un numero válido---')
            
        if selection_player == 1:
            return 'stand'

        if selection_player == 2:

           
            hand += deal()

            return hand

def automated_turn(hand:str,total:int,player:str) -> str:
    """ What the bot does in a turn of the match

    The bot will choose between stand or hit another card, 
    depending on the value of his hand.

    Args:
        hand (str): Hand of the bot
        player (str): The nickname of the bot that always will be crupier

    Returns:

        hand (str): Hand of the bot with one more card.
        stand (str): A string that will be treated later.
    """

    selection_player = None
    execute = False

    while selection_player != 1 or selection_player is None or execute is not False:

        if player == 'crupier':
            print(f'\nTurno de {player}')
            print('1.Plantarse \n2.Pedir carta\n-> ', end = '')
            while not execute and total <=17 :
                time.sleep(1)
                print('2\n', end = '')
                time.sleep(1)
                total = 0
                hand += deal()
                execute = True

                return hand
                
            if total > 17:
                time.sleep(1)
                print('1')
                time.sleep(1)
                return 'stand'
            
def clean_terminal():
    """Clean the terminal

    Will print in the terminal a command depending of the operating system.
    
    """
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
