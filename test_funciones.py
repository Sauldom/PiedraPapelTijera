import pytest


from funciones import *
from variables import LIST_PPT

def test_is_exit():

    assert is_exit("hola") == False
    assert is_exit("piedra")== False
    assert is_exit("cobarde")==True
    assert is_exit("") == False


def test_generate_computer_choice():
    
    assert generate_computer_choice() in LIST_PPT

def test_evaluate_move():

    assert evaluate_move('piedra', 'piedra') == 'Ha sido un empate piedra contra piedra'
    assert evaluate_move ('piedra', 'papel') == 'El robot gana con papel contra piedra'
    assert evaluate_move('tijera', 'papel') == 'El jugador gana con tijera contra papel'
    assert evaluate_move('piedra', 'papel') != ''