"""
    This file helped me to understand that my tic tac toe game works correctly!
    There are some tests which cover the different ways of the initialisation,
    game situations and the results of these situations.
    Also I check the situation where one stage of the game are copied.
"""

import unittest
from tic_tac_toe_game import *


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.file_with_test1 = open('test_data_directory/test_data1.txt', 'r')
        self.file_with_test1.readline()  # there is the service first line in the file with test data
        self.tic_tac_toe3 = TicTacToeGame.create_new_game(
            self.file_with_test1.readline().strip(),
            self.file_with_test1.readline().strip()
        )
        self.file_with_test2 = open('test_data_directory/test_data2.txt', 'r')
        self.file_with_test2.readline()
        self.tic_tac_toe4 = TicTacToeGame(
            self.file_with_test2.readline().strip(),
            self.file_with_test2.readline().strip()
        )

    def test_game_data_in_process_1(self):
        self.tic_tac_toe1 = TicTacToeGame('', '')
        self.assertEqual(self.tic_tac_toe1.player1_name, 'Player_A')
        self.assertEqual(self.tic_tac_toe1.player2_name, 'Player_B')
        self.assertEqual(self.tic_tac_toe1.game_data, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.tic_tac_toe1.make_move('X', 9)
        self.tic_tac_toe1.make_move('O', 1)
        self.assertEqual(self.tic_tac_toe1.game_data, ['O', 2, 3, 4, 5, 6, 7, 8, 'X'])
        self.tic_tac_toe1.make_move('X', 4)
        self.tic_tac_toe1.make_move('O', 3)
        self.tic_tac_toe1.make_move('X', 2)
        self.assertEqual(self.tic_tac_toe1.game_data, ['O', 'X', 'O', 'X', 5, 6, 7, 8, 'X'])
        self.tic_tac_toe1.make_move('O', 5)
        self.tic_tac_toe1.make_move('X', 7)
        self.tic_tac_toe1.make_move('O', 8)
        self.tic_tac_toe1.make_move('X', 6)
        self.assertEqual(self.tic_tac_toe1.game_data, ['O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'])
        self.assertEqual(self.tic_tac_toe1.check_winner(), False)

    def test_game_data_in_progress_2(self):
        self.tic_tac_toe2 = TicTacToeGame.create_new_game('Vasya', 'Petya')
        self.assertEqual(self.tic_tac_toe2.player1_name, 'Vasya')
        self.assertEqual(self.tic_tac_toe2.player2_name, 'Petya')
        self.assertEqual(self.tic_tac_toe2.game_data, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.tic_tac_toe2.make_move('X', 2)
        self.tic_tac_toe2.make_move('O', 5)
        self.assertEqual(self.tic_tac_toe2.game_data, [1, 'X', 3, 4, 'O', 6, 7, 8, 9])
        self.tic_tac_toe2.make_move('X', 1)
        self.tic_tac_toe2.make_move('O', 3)
        self.tic_tac_toe2.make_move('X', 6)
        self.assertEqual(self.tic_tac_toe2.game_data, ['X', 'X', 'O', 4, 'O', 'X', 7, 8, 9])
        self.tic_tac_toe2.make_move('O', 7)
        self.assertEqual(self.tic_tac_toe2.game_data, ['X', 'X', 'O', 4, 'O', 'X', 'O', 8, 9])
        self.assertEqual(self.tic_tac_toe2.check_winner(), 'O')

    def test_game_data_in_progress_3(self):
        self.assertEqual(self.tic_tac_toe3.player1_name, 'Ilia')
        self.assertEqual(self.tic_tac_toe3.player2_name, 'Anna')
        self.assertEqual(self.tic_tac_toe3.game_data, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        for i in range(2):
            temp_line = self.file_with_test1.readline().strip().split()
            self.tic_tac_toe3.make_move(temp_line[0], int(temp_line[1]))
        self.assertEqual(self.tic_tac_toe3.game_data, ['X', 'O', 3, 4, 5, 6, 7, 8, 9])
        for i in range(3):
            temp_line = self.file_with_test1.readline().strip().split()
            self.tic_tac_toe3.make_move(temp_line[0], int(temp_line[1]))
        self.assertEqual(self.tic_tac_toe3.game_data, ['X', 'O', 3, 4, 'X', 6, 'X', 8, 'O'])
        for i in range(2):
            temp_line = self.file_with_test1.readline().strip().split()
            self.tic_tac_toe3.make_move(temp_line[0], int(temp_line[1]))
        self.assertEqual(self.tic_tac_toe3.game_data, ['X', 'O', 'X', 'O', 'X', 6, 'X', 8, 'O'])
        self.assertEqual(self.tic_tac_toe3.check_winner(), 'X')

    def test_set_same_game(self):
        self.assertEqual(self.tic_tac_toe4.game_data, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(self.tic_tac_toe4.player1_name, 'Andrew')
        self.assertEqual(self.tic_tac_toe4.player2_name, 'Nastya')
        for i in range(9):
            temp_line = self.file_with_test2.readline().strip().split()
            self.tic_tac_toe4.make_move(temp_line[0], int(temp_line[1]))
        self.assertEqual(self.tic_tac_toe4.game_data, ['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O'])
        self.assertEqual(self.tic_tac_toe4.check_winner(), 'X')

        self.tic_tac_toe_copy = TicTacToeGame.create_same_game(self.tic_tac_toe4)
        self.assertEqual(self.tic_tac_toe_copy.player1_name, 'Andrew')
        self.assertEqual(self.tic_tac_toe_copy.player2_name, 'Nastya')
        self.assertEqual(self.tic_tac_toe_copy.game_data, ['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O'])
        self.assertEqual(self.tic_tac_toe_copy.check_winner(), 'X')

    def tearDown(self) -> None:
        self.file_with_test1.close()
        self.file_with_test2.close()
