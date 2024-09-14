"""
    hacer importaciones.
    
    """

from .tools import random_number, comparison, record_numbers, end_game, start_game
from .players import players, validate_number
from .system_turn import system_turn


user_list = []
system_list = []

def game():
    """
    Función principal que inicia el juego, generando un número aleatorio
    y llamando a otras funciones necesarias para la lógica del juego.
    """
    start_game()
    number = random_number()  # Genera un número aleatorio para el juego

    while True:  # Bucle principal del juego
        print("-------------user turn----------------")

        user_number = players()  # Llamada a la función 'players' y asignación a 'user_number'
        validate_number(user_number)  # Valida el número ingresado por el usuario
        record_user = record_numbers(user_number, user_list)  # Registra el número del usuario

        if user_number == number:  # Verifica si el número es igual
            end_game('Usuario', record_user)
            break  # Rompe el bucle al adivinar correctamente
        else:
            comparison(user_number, number)

        print("------------system turn--------------")
        system_number = system_turn()
        record_system = record_numbers(system_number, system_list)

        if system_number == number:  # Verifica si el sistema adivina
            end_game('Sistema', record_system)
            break  # Rompe el bucle si el sistema adivina correctamente
        else:
            comparison(system_number, number)

if __name__ == '__main__':
    game()
