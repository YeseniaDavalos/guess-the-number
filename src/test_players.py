"""
Módulo de pruebas para el módulo players del proyecto Guess-the-Number.
Contiene pruebas unitarias para validar las funciones players y validate_number.
"""

import unittest
from unittest import mock
import sys
from src.players import players, validate_number  # Mantenemos el import después de añadir la ruta

# Agregar ruta para src
sys.path.append('./src')



class TestPlayers(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para las funciones del módulo players.py.
    """

    def test_players_valid_input(self):
        """
        Test que simula la entrada de un número válido.
        """
        with mock.patch('builtins.input', return_value='50'):
            self.assertEqual(players(), 50)

    def test_players_invalid_input(self):
        """
        Test que simula la entrada de un valor no numérico.
        Debemos comprobar que sigue pidiendo un número válido.
        """
        with mock.patch('builtins.input', side_effect=['abc', '50']):
            self.assertEqual(players(), 50)

    def test_validate_number_valid(self):
        """
        Test que comprueba si el número válido es aceptado por la función validate_number.
        """
        self.assertEqual(validate_number(50), 50)

    def test_validate_number_invalid_low(self):
        """
        Test que verifica si un número por debajo del rango (1) es rechazado.
        """
        with mock.patch('builtins.input', return_value='50'):
            self.assertEqual(validate_number(0), "Ingresa un número válido")

    def test_validate_number_invalid_high(self):
        """
        Test que verifica si un número por encima del rango (100) es rechazado.
        """
        with mock.patch('builtins.input', return_value='50'):
            self.assertEqual(validate_number(101), "Ingresa un número válido")

if __name__ == '__main__':
    unittest.main()
