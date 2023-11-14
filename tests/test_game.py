import pytest
from src.game import *

def test_player(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Naruto53')
    result = player()
    assert result == 'Naruto53'

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
