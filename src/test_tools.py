"""
Módulo de pruebas para el archivo tools del proyecto Guess the Number.
Contiene pruebas unitarias para las funciones del archivo tools.py.
"""

import unittest
from unittest import mock
from src.tools import random_number, comparison, record_numbers, start_game, end_game


class TestTools(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para las funciones de tools.py.
    """

    def test_random_number(self):
        """
        Test que verifica si la función random_number devuelve un número entre 1 y 100.
        """
        for _ in range(1000):
            number = random_number()
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 100)

    def test_comparison_guess_lower(self):
        """
        Test para verificar que cuando la suposición es menor, imprime el mensaje adecuado.
        """
        with mock.patch('builtins.print') as mocked_print:
            comparison(50, 100)
            mocked_print.assert_called_with("El número es mayor")

    def test_comparison_guess_higher(self):
        """
        Test para verificar que cuando la suposición es mayor, imprime el mensaje adecuado.
        """
        with mock.patch('builtins.print') as mocked_print:
            comparison(100, 50)
            mocked_print.assert_called_with("El número es menor")

    def test_record_numbers(self):
        """
        Test para verificar que la función record_numbers.
        """
        record_list = []
        record_numbers(50, record_list)
        self.assertIn(50, record_list)
        self.assertEqual(len(record_list), 1)

    def test_start_game(self):
        """
        Test que verifica si la función start_game imprime las instrucciones correctamente.
        """
        with mock.patch('builtins.print') as mocked_print:
            start_game()
            mocked_print.assert_any_call("Bienvenido al juego Guess the Number")
            mocked_print.assert_any_call("Adivina un numero al azar entre el 1 y 100")

    def test_end_game(self):
        """
        Test que verifica si la función end_game imprime el mensaje adecuado al finalizar el juego.
        """
        with mock.patch('builtins.print') as mocked_print:
            end_game("Jugador", [50, 75, 100])
            mocked_print.assert_any_call("correcto!! Jugador acertaste el numero")
            mocked_print.assert_any_call("Registro de números [50, 75, 100]")


if __name__ == '__main__':
    unittest.main()
