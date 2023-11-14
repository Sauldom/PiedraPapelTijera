from variables import LIST_PPT, EXIT
import random

def read_user_choice():
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario
    """
    usr_choice=''
    print("Bienvenido al juego:\n")
    print("Escribe: piedra, papel o tijera para jugar\n")
    print("Puedes escribir cobarde para acabar:\n")
    
    
    while usr_choice not in LIST_PPT and usr_choice != EXIT:
        usr_choice = input("elige bien humano: ")
        usr_choice = usr_choice.lower()
    return  usr_choice

#read_user_choice()

def is_exit(usr_choice):
    """
    Predicado que recib ela respuesta del usuario y devuelve `True` si
    ha pedido salir del juego
    """
    salida = False
    if usr_choice == EXIT:
        salida = True
    return salida

def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatroia. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    aleatorio = random.randint(0,2)

    return LIST_PPT[aleatorio]

def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    winner=''
    #papel gana a piedra  piedra gana tijeras tijeras gana papel
    
    if user_choice == computer_choice:
        winner='Ha sido un empate {} contra {}'.format(user_choice, computer_choice)
    elif (user_choice =='papel' and computer_choice=='piedra') or(user_choice =='piedra' and computer_choice=='tijera') or(user_choice =='tijera' and computer_choice=='papel'):
        winner = 'El jugador gana con {} contra {}'.format(user_choice,computer_choice)
    else:
        winner = 'El robot gana con {} contra {}'.format(computer_choice,user_choice)

    return winner

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print ('El resultado queda así:\n')
    print('-------------')
    print (result)
    print('----------\n')
    return None 


