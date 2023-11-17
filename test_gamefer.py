import pytest
from enum import Enum
from gamefer import evaluate_move



class UserChoice(Enum):
    INVALID_CHOICE = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3

def test_evaluate_move():

    class UserChoice(Enum):
        INVALID_CHOICE = -1
        PAPER = 0
        ROCK = 1
        SCISSORS = 2
        QUIT = 3
    assert evaluate_move(UserChoice.PAPER, UserChoice.PAPER) == 'empate'
    assert evaluate_move(UserChoice.PAPER, UserChoice.ROCK)=='jugador'
    assert evaluate_move(UserChoice.PAPER, UserChoice.SCISSORS)=='cpu'