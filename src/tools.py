'''
guess the number
'''
from random import randint

def random_number():
    """
    Genera un número aleatorio entre 1 y 100.

    Returns:
    int: Número aleatorio entre 1 y 100.
    """


    number = randint(1, 100)  # Sin espacios extra al final de la línea
    return number

def comparison(guess, number):
    """
    compara la suposicion del jugador con el numero arrojado por el sistema

    parametros: 
    guess(int): suposicion de los jugadores
    number(int): numero que arroja el sistema
    """
    if guess < number:  # Elimina los espacios en blanco después de los dos puntos
        print("El número es mayor")  # Elimina los espacios en blanco al final
    elif guess > number:  # Elimina los espacios en blanco después de los dos puntos
        print("El número es menor")  # Elimina los espacios en blanco al final


def record_numbers(number, record_list):
    """
    introduce los numeros de los jugadores en una lista para llevar un registro

    parametros: 
    number(int): suposicion de los jugadores
    record_list([]): listas vacias donde se van introduciendo los numeros
    """
    record_list.append(number)
    return record_list

def start_game():
    """
    Inicia el juego 'Guess the Number' e imprime las instrucciones.

    Muestra un mensaje de bienvenida e instrucciones para adivinar un número entre 1 y 100.
    """
    #inicio de juego
    print("Bienvenido al juego Guess the Number")
    print("Adivina un numero al azar entre el 1 y 100")


def end_game(winner, record_list):
    """
    fin del juego

    parametros: 
    winner(str): quien gano el usuario o la computadora
    record_list([]): lista de registro del ganador
    """
    print(f"correcto!! {winner} acertaste el numero")
    print(f"Registro de números {record_list}")  # Esta es la línea final del código


# Nueva línea agregada aquí
