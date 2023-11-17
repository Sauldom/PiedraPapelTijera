
from enum import Enum

# User choices
class UserChoice(Enum):
    INVALID_CHOICE = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3

def game_loop()->None:
    """
    Arranca el bucle principal del juego
    """
    

    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice()->UserChoice:
    """
    Lee la jugada del humano, que además d epiedra, papel o tijera
    podría sedr la de salir del juego
    """
    user_choice = UserChoice.INVALID_CHOICE
    while user_choice == UserChoice.INVALID_CHOICE:
        print('Select one number:')
        print(f'{UserChoice.PAPER.value}. Paper')
        print(f'{UserChoice.ROCK.value}. Rock')
        print(f'{UserChoice.SCISSORS.value}. Scissors')
        print('-------------------')
        print(f'{UserChoice.QUIT.value}. Quit the game')

        try:
            user_choice = UserChoice(int(input('Enter your choice:')))
        except ValueError:
            user_choice = UserChoice.INVALID_CHOICE


       
        
    return user_choice 

def is_exit(game_choice: UserChoice)->bool:
    """
    Predicado que determina si la jugada es la opción de salir pitando
    """
    return game_choice == UserChoice.QUIT

def generate_computer_choice()->UserChoice:
    """
    Genera una jugada del ordenador al azar y la devuelve
    """
    from random import choice
    return choice([UserChoice.PAPER, UserChoice.ROCK, UserChoice.SCISSORS])

def evaluate_move(user_choice: UserChoice, computer_choice: UserChoice)->str:
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    """
    win =''
    if user_choice == computer_choice:
        win = 'empate'
        
    elif (user_choice.value ==0 and computer_choice.value==1) or (user_choice.value == 1 and computer_choice.value==2) or (user_choice.value == 2 and computer_choice.value==0):
        win ='jugador gana con ' + user_choice.name + ' contra '+ computer_choice.name
    else:
        win ="cpu gana con " + computer_choice.name + ' contra '+ user_choice.name
    

    return win


def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print('\n \n----------------\n')
    print('El resultado es')
    print(result)
    print('\n -----------------\n')
    return None # pa que te calles!

if __name__ == "__main__":
    # no me han importado, me llamaron desde la linea de
    # comandos: arranco el juegolllll!
    game_loop()




