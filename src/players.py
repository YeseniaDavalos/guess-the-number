"""
Este módulo contiene funciones para un juego de adivinanza de números.
Los jugadores deben adivinar un número entre 1 y 100.
Incluye validaciones para asegurar que los jugadores introduzcan números válidos.
"""

def players():
    """
    Función que permite al usuario introducir sus suposiciones.
    Bucle que permite que se ingresen solo números enteros.
    """
    while True:
        input_number = input("Introduce un número: ")  # Se eliminó el trailing whitespace
        try:
            user_number = int(input_number)
            return user_number
        except ValueError:
            print("Ingresa un número válido")


def validate_number(number):
    """
    Función que valida que el número ingresado esté 
    dentro de los parámetros establecidos.
    """
    if number < 1 or number > 100:
        print("Ingresa un número válido")
        players()
        return "Ingresa un número válido"
    return number


# Agrega una nueva línea en blanco aquí (presiona Enter)
