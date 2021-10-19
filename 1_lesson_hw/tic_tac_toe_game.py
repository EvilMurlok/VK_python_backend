"""
    This is a standard 3x3 tic-tac-toe game between two players.
    People will need to enter your names depends on
    who will be for crosses and who will be for zeroes.
    The first ones start, of course, with crosses.
    Then everything happens according to the usual rules: the players enter a number from 1 to 9,
    depending on the field where they want to place a cross/zero.
    The winner is the one who collects 3 in a row/diagonal.
"""


class ValidString:
    """A descriptor providing valid data in string fields"""

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name)

    def __set__(self, instance, player_name):
        if isinstance(player_name, str):
            instance.__dict__[self.property_name] = player_name
        else:
            raise ValueError(f'{self.property_name} must be a string '
                             f'but {type(player_name).__name__} was given!')


class ValidGameData:
    """A descriptor providing valid data in game data field"""

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name)

    def __set__(self, instance, game_data=None):
        if game_data is None:
            instance.__dict__[self.property_name] = list(range(1, 10))
        elif isinstance(game_data, list):
            instance.__dict__[self.property_name] = game_data
        else:
            raise ValueError(f'{self.property_name} must be a list '
                             f'but {type(game_data).__name__} was given!')


class TicTacToeGame:
    """The class in which the game of tic-tac-toe is implemented"""
    player1_name = ValidString()
    player2_name = ValidString()
    game_data = ValidGameData()

    @staticmethod
    def greeting_players():
        print('You will need to enter your names depends on '
              'who will be for crosses and who will be for zeroes'
              ' so that you can distinguish between the two players.\n'
              'You can see a 3x3 field with the numbers of the cells for your moves. ')
        print('-------------')
        for i in range(3):
            print('|', 1 + i * 3, '|', 2 + i * 3, '|', 3 + i * 3, '|')
            print('-------------')
        print('Each one in turn enters the number where he wants to place his sign. '
              'The winner is the one who collects 3 in a row/column/diagonal.')
        input('Enter to continue!')

    @staticmethod
    def get_name(number_of_person):
        if number_of_person not in (1, 2):
            raise ValueError('This value must be equal 1 or 2, '
                             'because this game is for two people!')
        temp_name = input(f'Input the name of the {number_of_person} player: ')
        if number_of_person == 1:
            return temp_name if temp_name else 'Player_A'
        return temp_name if temp_name else 'Player_B'

    def __init__(self, player1_name, player2_name, game_data=None):
        self.player1_name = player1_name if player1_name else 'Player_A'
        self.player2_name = player2_name if player2_name else 'Player_B'
        self.game_data = game_data

    @classmethod
    def create_new_game(cls, name1, name2):
        return cls(name1, name2)

    @classmethod
    def create_same_game(cls, obj):
        if hasattr(obj, 'player1_name') and \
                hasattr(obj, 'player2_name') and \
                hasattr(obj, 'game_data'):
            name1, name2, game_data = getattr(obj, 'player1_name'), \
                                      getattr(obj, 'player2_name'), \
                                      getattr(obj, 'game_data')
            return cls(name1, name2, game_data)
        else:
            return cls

    def __get_user_move(self, required_sign):
        flag = False
        while not flag:
            user_input = input(f'On what position will we draw {required_sign}? '
                               f'(input integer in [1; 9]:\t')
            try:
                user_input = int(user_input)
            except ValueError:
                print('\u001b[1;31mBe careful and input only digits (1-9)!!!\u001b[0;0m')
                continue
            if user_input < 1 or user_input > 9:
                print('\u001b[9;31mYou are stupid!\u001b[0;0m '
                      '\u001b[1;31mPlease, enter the integer in [1; 9]\u001b[0;0m')
            else:
                if str(self.game_data[user_input - 1]) not in 'XO':
                    return user_input
                else:
                    print('\u001b[9;31mOH, MY GOD!\u001b[0;0m '
                          '\u001b[1;31mThis cell is already taken! '
                          'Try again!\u001b[0;0m')

    def check_winner(self):
        win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                          (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for condition in win_conditions:
            if self.game_data[condition[0] - 1] == \
                    self.game_data[condition[1] - 1] == \
                    self.game_data[condition[2] - 1]:
                return self.game_data[condition[0] - 1]
        return False

    def show_playground(self):
        print('The current situation in the playground:')
        print('-------------')
        for i in range(3):
            print('|', self.game_data[0 + i * 3], '|',
                  self.game_data[1 + i * 3], '|',
                  self.game_data[2 + i * 3], '|')
            print('-------------')

    def make_move(self, required_sign, user_input):
        self.game_data[user_input - 1] = required_sign

    def play_the_game(self):
        turn = 1
        flag = False
        while not flag:
            self.show_playground()
            if turn % 2:
                self.make_move('X', self.__get_user_move('X'))
            else:
                self.make_move('O', self.__get_user_move('O'))
            turn += 1
            if turn > 5:
                winner_sign = self.check_winner()
                if winner_sign and winner_sign == 'X':
                    print(f'\u001b[1;32mCongratulations!\u001b[0;0m '
                          f'Player \u001b[1;32m{self.player1_name}\u001b[0;0m wins this game! '
                          f'\u001b[1;31m{self.player2_name}\u001b[0;0m, you must train better!')
                    break
                elif winner_sign and winner_sign == 'O':
                    print(f'\u001b[1;32mCongratulations!\u001b[0;0m '
                          f'Player \u001b[1;32m{self.player2_name}\u001b[0;0m wins this game! '
                          f'\u001b[1;31m{self.player1_name}\u001b[0;0m, you must train better!')
                    break
            if turn == 10:
                print(f'\u001b[1;34mThe tie\u001b[0;0m between '
                      f'\u001b[1;34m{self.player1_name}\u001b[0;0m '
                      f'and \u001b[1;34m{self.player2_name}\u001b[0;0m!')
                break
        self.show_playground()


def main():
    print('Hello in my tic-tac-toe game, dear friends!')
    user_wish = input('Do you want to play the game?(y/n)\t').lower()
    info, flag = True, user_wish == 'y'
    while flag:
        player1_name, player2_name = TicTacToeGame.get_name(1), TicTacToeGame.get_name(2)
        ttt = TicTacToeGame.create_new_game(player1_name, player2_name)
        if info:
            ttt.greeting_players()
            info = False
        ttt.play_the_game()
        user_wish = input('Do you want to play the game?(y/n)\t').lower()
        flag = user_wish == 'y'


if __name__ == '__main__':
    main()
