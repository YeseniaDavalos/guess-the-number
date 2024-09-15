"""
Este módulo contiene pruebas unitarias para el juego.
"""

import unittest
from unittest.mock import patch
from src.game import game


class TestGame(unittest.TestCase):
    """
    Esta clase contiene pruebas unitarias para la función `game` en el módulo `src.game`.
    """

    @patch('src.tools.random_number')
    @patch('src.players.players')
    @patch('src.tools.end_game')
    @patch('src.system_turn.system_turn')
    @patch('src.tools.record_numbers')
    def test_game_user_wins(self, mock_record_numbers, mock_system_turn,
                            mock_end_game, mock_players, mock_random_number):
        """
        Prueba.
        """
        mock_random_number.return_value = 5
        mock_players.return_value = 5
        mock_record_numbers.return_value = [5]
        game()
        mock_end_game.assert_called_with('Usuario', [5])
        mock_system_turn.assert_not_called()

    @patch('src.tools.random_number')
    @patch('src.players.players')
    @patch('src.tools.end_game')
    @patch('src.system_turn.system_turn')
    @patch('src.tools.record_numbers')
    def test_game_system_wins(self, mock_record_numbers, mock_system_turn,
                              mock_end_game, mock_players, mock_random_number):
        """
        Prueba.
        """
        mock_random_number.return_value = 5
        mock_players.return_value = 3
        mock_system_turn.return_value = 5
        mock_record_numbers.return_value = [5]
        game()
        mock_end_game.assert_called_with('Sistema', [5])

    @patch('src.tools.random_number')
    @patch('src.players.players')
    @patch('src.system_turn.system_turn')
    @patch('src.tools.comparison')
    def test_game_comparison_called(self, mock_comparison, mock_system_turn,
                                    mock_players, mock_random_number):
        """
        Prueba que la función de comparación se llama correctamente cuando 
        tanto el usuario como el sistema no adivinan el número.
        """
        mock_random_number.return_value = 5
        mock_players.return_value = 3
        mock_system_turn.return_value = 4
        game()
        mock_comparison.assert_any_call(3, 5)
        mock_comparison.assert_any_call(4, 5)

if __name__ == '__main__':
    unittest.main()
