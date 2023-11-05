import random
import os
import time 

def player():

    return input('Introduce tu nombre -> ')

def deal():

    deck = 'A234567890JKQ' 

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
"""
Cada vez que la función se ejecuta, se relee toda la cadena de caracters y se vuelven a sumar sus valores.Principalmente 
para cuando la letra A que tiene doble valor, se escoja el que más convenga. 
Ejemplo:

A3 -> La A valdra 11, retornando la función 11
A38 -> Como en esta ocasión, si la A vale 11, la función retornaría 22, cosa que el jugador no le conviene.
Por tanto se retornaría como 12 debido a que la A puede valer 1, en función de como le conviene al jugador.

"""

def cases(hand1, hand2,player1, player2, total1, total2, turn_counter):
    
    if total1 > 21:
        if total2 > 21:
            resultado = 'Game over. ¡Los dos la habeis pifiado!'

        else:
            resultado = f'¡Gana J2 - {player2}!'
      
    elif total2 > 21:
        resultado = f'¡Gana J1 - {player1}!'
  
    else:
        difference1 = abs(21 - total1)
        difference2 = abs(21 - total2)

        if difference1 == difference2:
            resultado = '¡EMPATE!'

        elif difference1 < difference2:
            resultado = f'¡Gana J1 - {player1}!'
        else:
            resultado = f'¡Gana J2 - {player2}!'


    return (f'JUEGO TERMINADO - Ronda {turn_counter}\n' +
            f'{resultado}\n' +
            f'J1 - {player1} - {hand1} ({total1})\n' +
            f'J2 - {player2} - {hand2} ({total2})\n')

"""
    En esta función se introduce la mano del jugador 1 y 2, sus respectivos nombres, el total de cada jugador y el contador
    de rondas.

    En total solo se pueden dar 4 casos:

    1º caso:
        Los dos jugadores se pasen de 21
    2º caso:
        Que los dos jugadores empaten
    3º caso:
        Que gane el jugador 1
    4º caso:
        Que gane el jugador 2

    Para simplficar el código cada situación carga un valor distinto en la variable resultado que cambia el título de la acción
    en concreto, más adelante en el return

    También se ha utilizado una resta absoluta de 21 con el total de cada jugador, ya que permite más precisión a la hora de tratar
    los datos.
    """


def turn(hand1,total1,player1):

    selection_player = None
    
    while selection_player != 1 or selection_player != 2 or selection_player is None:
        
        print(f'\nTurno de {player1}')
        selection_player = input('1.Plantarse \n2.Pedir carta\n-> ')
        if selection_player.isnumeric():
            selection_player = int(selection_player)

        else:
            print('---Introduce un numero válido---')
            
        if selection_player == 1:
            return 'plantarse'

        if selection_player == 2:

           
            hand1 += deal()

            return hand1
"""
Un jugador normal, el cual bajo su propio juicio decide la decisión de si plantarse o pedir carta.. 
Si elige 2 (pedir carta) llamara la función deal() y lo sumara a la mano actual del jugador.
Despues esta nueva mano, es retornada a la función.

Si elige 1 (plantarse) la funcion retorna plantarse para que el programa donde sea llamada, trate la información como se prefiera.
"""
        
def automated_turn(hand1,total1,player1):
    selection_player = None
    execute = False

    while selection_player != 1 or selection_player is None or execute is not False:

        if player1 == 'crupier':
            print(f'\nTurno de {player1}')
            print('1.Plantarse \n2.Pedir carta\n-> ', end = '')
            while not execute and total1 <=17 :
                time.sleep(1)
                print('2\n', end = '')
                time.sleep(1)
                total1 = 0
                hand1 += deal()
                execute = True

                return hand1
                
            if total1 > 17:
                time.sleep(1)
                print('1')
                time.sleep(1)
                return 'plantarse'
"""
Si el nombre del jugador que interactua con la función es 'crupier', juegue de manera automática
según las instrucciones que se ha programado que es la que los crupieres reales suelen usar en la vida real, bajo normas del casino.

Mientras el total de sus cartas sea igual o inferior a 17, siga cogiendo cartas y si su total es mayor a 17 que retorne plantarse
y ya en el programa donde se llame la función se tratara esa información.
"""
            
def clean_terminal():
    """
    Esta función es para limpiar la terminal durante la ejecución, ese condicional es para que pueda ejecutarse
    tanto como en windows 
    """
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
