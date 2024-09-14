"""
Este módulo contiene la lógica para que el sistema elija un número aleatorio en el juego.
"""

from random import randrange

def system_turn():
    """
    Función que genera un número aleatorio para el sistema y lo imprime.

    Returns:
        int: El número aleatorio generado por el sistema.
    """
    # Arroja un número aleatorio del sistema
    system_number = randrange(1, 100, 1)
    system_decision = f"El número del sistema es {system_number}"
    print(system_decision)
    return system_number


# Nueva línea agregada aquí
