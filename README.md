<p style="text-align: center;"><b>VITRUVIAN'S MAN'S</b></p>

---

<p align="center">
    <img width="400" height="400" src="/image/Vitruvian1.jpeg">
</p>

## EXPLICACIÓN BLACKJACK VITRUVIAN'S MAN'S

```
El archivo principal es el denominado Blackjack.py, este 
sera el que ejecutemos para jugar al blackjack.Los otros archivos, son 
archivos externos de los cuales se importan funciones para mantener un entorno de trabajo 
más ordenado
```

## FUNCIONAMIENTO BLACKJACK VITRUVIAN'S MAN'S

```
En este documento analizaremos y explicaremos la manera en la que funciona 
el programa.Para que sea más sencillo, 
seguiremos el flujo del programa para explicarlo.Tenemos 4 archivos, 
que contienen funciones y un archivo donde se realizan los tests de las funciones.
```

Estos cuatro archivos se encuentran situados en la carpeta src *(source)* siendo:

* Blackjack.py
* game.py
* oneplayer.py
* twoplayers.py

El archivo más importante es el que recibe el nombre game.py ya que es el que contiene la gran mayoría de funciones que se utilizaran a lo largo de este blackjack.

### GAME.PY

---

##### Player()

```
def player():

    return input('Introduce tu nombre -> ')

```

Simplemente. retornara el nombre de usuario que haya decidido ponerse.

##### Deal()

```python
def deal():

    deck = 'A234567890JKQ' 

    return deck[random.randint(0,12)]
```

El cometido de esta función es devolver un caracter aleatorio de los que componen la cadena de texto

##### Total_value()

```python
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
```

Esta función se le introduce el valor de la mano de un jugador.El bucle for se encarga de recorrer cada caracter de la cadena de texto que forma la mano y busca su equivalencia númerica.

Las equivalencias son:

* J,K,Q,0 = 10
* A = 11 o 1 (Se toma de los dos, el valor que más convenga al jugador)
* 2,3,4,5,6,7,8,9 = A si mismo

Cuando ha recorrido todos los carácteres, la función retorna el total en una variable con el mismo nombre.

##### Cases()

```python
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

```

Para que esta función pueda funcionar nos hara falta la mano de ambos jugadores, sus nombres, el valor númerico de su mano y el valor del contador (se tiene en cuenta fuera de la función)

En total solo se pueden dar 4 casos:

    1º caso:
   	 Los dos jugadores se pasen de 21

    2º caso:
    	Que los dos jugadores empaten

    3º caso:
    	Que gane el jugador 1

    4º caso:
    	Que gane el jugador 2

Para simplficar el código cada situación carga un valor distinto en la variable resultado que cambia el título de la acción en concreto, más adelante en el return

También se ha utilizado una resta absoluta de 21 menos el total de cada jugador, ya que permite más precisión a la hora de tratar los datos.

##### Turn()

```python
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
```

Un jugador normal, el cual bajo su propio juicio decide la decisión de si plantarse o pedir carta.

Si elige 2 (pedir carta) llamara la función deal() y lo sumara a la mano actual del jugador. Despues esta nueva mano, es retornada a la función.

Si elige 1 (plantarse) la funcion retorna plantarse para que el programa donde sea llamada, trate la información como se prefiera. Mientras el jugador no escoja una de las dos opciones que se le ofrecen, se le pedira introducir de nuevo una respuesta.

##### Automated_turn()

```python
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
```

Si el nombre del jugador que interactua con la función es 'crupier', juegue de manera automática según las instrucciones que se ha programado que es la que los crupieres reales suelen usar en la vida real, bajo normas del casino.

Mientras el total de sus cartas sea igual o inferior a 17, siga cogiendo cartas y si su total es mayor a 17 que retorne plantarse y ya en el programa donde se llame la función decidira como tratar esa información.

##### Clean_terminal()

```python
def clean_terminal():
if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
```

Esta función es para limpiar la terminal durante la ejecución, ese condicional es para que pueda ejecutarse tanto en linux como en windows.

---

### BLACKJACK.PY

---

Una vez explicado, como funcionan la mayoría de funciones que se iran viendo a lo largo del programa. Seguiremos el flujo del mismo y comentando su funcionamiento.

##### Modo_Juego()

```python
from twoplayers import match_twoplayers
from oneplayer import match_1player
from game import clean_terminal

def modo_juego():
  
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
```

En esta función llamada *Modo_Juego()*, nos encontramos con una variable llamada election = None

Luego un bucle, con dos condiciones a cumplir que son que mientras election sea distinto de 1 o 2, el programa debera seguir ejecutandose.

Ahora una variable llamada user_input almacena la respuesta del usuario que la tratara siguiendo los condicionales. Comprueba que sea numerico y sino es ni 1 ni 2 u otro valor (string), volvera a empezar el bucle.

##### main()

```python
def main():

    election = modo_juego()

    if election == 1:
  
        match_twoplayers()
   
    else:
        match_1player()
```

En el main de este archivo, se guarda en una variable llamada *election,* la respuesta del usuario, el cual dependiendo de lo que haya elegido, llamara a la función main de un archivo u de otro, eligiendo así un modo de juego y ejecutando su partida

---

### Match_twoplayers()

---

Debido a la extensión, dividiremos el código para una mejor explicación

```python
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
```

El código empieza importando las funciones del archivo game.py.

Luego define la función y empieza a definir las variables que se usaran a lo largo de la partida, como son los nicknames de los usuarios, su  mano y correspondiente valor númerico

Se declara el contador de turnos, siendo 1 ya que esta asignación es considerada el turno 1.

Stand_player son variables que se usaran para conocer si el jugador decide plantarse o seguir.

Pifiada es una variable que controla el flujo para que cuando el total del jugador 1 sea superior a 21, de por finalizada la partida.

```python
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

```

Las condiciones para que el bucle while siga ejecutandose son las siguientes:

* Mientras stand_player1 y stand_player2 no sean el contrario (es decir, true)
* Que el total del jugador 1 y el total del jugador 2 no sean superiores a 21
* Y la variable pifia no valga False

Si se incumple una, el bucle finalizara y con ello la partida.

Luego se llama a la función call_terminal() para limpiar la pantalla.

Se comprueba si el jugador se ha plantado o no, si no se ha plantado, se llama a la funcion turn() con los valores de la mano y su correspondiente valor númerico.

Si el jugador se planta, la variable stand_player se le asigna el valor True y no jugara más turnos, hasta que el siguiente jugador tambien decida plantarse y con ello acabar la partida.

Si el total numerico de las cartas de la mano del jugador 1 es superior a 21, se cambia el valor de pifiada a False y cerrando así la partida.

Se hace lo mismo para el jugador 2, cuando acabe su turno, el contador aumenta en 1, así hasta que el bucle se rompa y con ello se llame la función cases() e imprima por pantalla la situación de la partida.

---

### Match_oneplayer()

---

Esta función se parece mucho a la anterior pero cuenta con una gran diferencia y es que aquí, juega una persona contra el programa. Eso incluye algunos cambios en el código que son los que nos disponemos a comentar.

```python
    player1 = player()
    player_crupier = 'crupier' #trata al crupier, la máquina, como si fuera un 2 jugador automatizado.

    player1_hand = deal()
    crupier_hand = deal()

    total_player1 = total_value(player1_hand)
    total_crupier = total_value(crupier_hand)

    turn_counter = 1
  
    stand_player1 = False
    stand_player2 = False
    pifiada = True

    clean_terminal()
```

Asigna el nickname de crupier a la variable player_crupier ya que para optimizar las funciones, sera tratado como un segundo jugador aunque este, no requiera de intervención humana para jugar en la partida.

```python
    while not (stand_player1 and stand_player2) and (total_player1 <= 21 and total_crupier <= 21) and pifiada == True:
        stand_player1 = False
        stand_player2 = False

        clean_terminal()

        print(f'Ronda {turn_counter}')
        print(f'J1 - {player1} - {player1_hand} ({total_player1})')
        print(f'J2 - {player_crupier} - {crupier_hand} ({total_crupier})') 

        if not stand_player1:
            result_player1 = turn(player1_hand, player1)
            if result_player1 == 'plantarse':
                stand_player1 = True
            else:
                player1_hand = result_player1
                total_player1 = total_value(player1_hand)

        if total_player1 > 21:
            pifiada = False

        elif not stand_player2:
            result_player2 = automated_turn(crupier_hand, total_crupier, player_crupier) #esta función es el que utiliza la máquina para jugar automáticamente
            if result_player2 == 'plantarse':
                stand_player2 = True
            else:
                crupier_hand = result_player2
                total_crupier = total_value(crupier_hand)

        turn_counter += 1

    print(cases(player1_hand, crupier_hand, player1, player_crupier, total_player1, total_crupier, turn_counter))

```

Lo que cambia es que aquí el jugador2, que es el crupier, utilizara la función automated_turn.

---

# TESTS

Dentro de la carpeta de tests se puede encontrar, el archivo test_game.py que contiene los tests de las funciones del archivo game.py

Hay tests de 3 funciones:

* De la función player()
* De la función cases()
* De la función total_value()

##### Test_player()

---

```python
def test_player(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Naruto53')
    result = player()
    assert result == 'Naruto53'
```

Para ello hemos utilizado un objeto dummy para probar un valor cualquiera, este input no tienen ninguna restricción.

##### Test_cases()

---

```python
import pytest
@pytest.mark.parametrize(
    ('hand1, hand2,player1, player2, total1, total2, turn_counter, expected'),
    [
        ('Q5','4230','Naruto532','PokemonMaster',15,19,4, 'JUEGO TERMINADO - Ronda 4\n' + '¡Gana J2 - PokemonMaster!\n' + 
         'J1 - Naruto532 - Q5 (15)\n' + 
         'J2 - PokemonMaster - 4230 (19)\n'),

         ('39Q','A4','Boruto3','AshKetchum',22,15,3, 'JUEGO TERMINADO - Ronda 3\n' + '¡Gana J2 - AshKetchum!\n' + 
         'J1 - Boruto3 - 39Q (22)\n' + 
         'J2 - AshKetchum - A4 (15)\n'),

         ('K3','A97','Goku123','OnePieceKing',13,17,4, 'JUEGO TERMINADO - Ronda 4\n' + '¡Gana J2 - OnePieceKing!\n' + 
          'J1 - Goku123 - K3 (13)\n' + 
          'J2 - OnePieceKing - A97 (17)\n'),

         ('K4','Q31','Legendary59','Bobobo',14,14,4, 'JUEGO TERMINADO - Ronda 4\n' +'¡EMPATE!\n' + 
          'J1 - Legendary59 - K4 (14)\n' + 
          'J2 - Bobobo - Q31 (14)\n'),

          ('90','K3','DiegoCano','Revilofe',19,13,4, 'JUEGO TERMINADO - Ronda 4\n' +'¡Gana J1 - DiegoCano!\n' + 
          'J1 - DiegoCano - 90 (19)\n' + 
          'J2 - Revilofe - K3 (13)\n')  
    ]
)
def test_cases_params(hand1, hand2,player1, player2, total1, total2, turn_counter,expected):
    assert cases(hand1, hand2,player1, player2, total1, total2, turn_counter) == expected
```

Hemos comprobado todos los casos que puede tener la función cases usando @pytest.mark.parametrize.

Hemos puesto los parametros que haran falta para la prueba unitaria y luego hemos definido esos parametros para el test.

##### Test_total_value()

---

```python
@pytest.mark.parametrize(
    'hand, expected',
    [
        ('Q56',21),
        ('KQ2',22),
        ('45',9),
        ('76A',14)
    ]
)
def test_total_value_params(hand,expected):
    assert total_value(hand) == expected
```

Lo hemos realizado de la misma manera que el anterior, para asi comprobar que todo funcione de manera correcta.
