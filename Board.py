from Player import Player


class Board:
    board_game = []

    def __init__(self):
        self.board_game = [None] * 24

    def add_player(self, un, pw, color, ID):
        player = Player(un, pw, color, ID)
        return player
        # color_code = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow'}
        # user_name = input('Username :')
        # password = input('Password :')
        # print(f'color :\n 1-red\t2-blue\t3-green\t4-yellow')
        # color_number = int(input('enter number of color :'))
        # print('----------------------------------------------------')
        # if color_number not in [1, 2, 3, 4]:
        #     print('invalid input')
        # else:
        #     if Player.colors_in_use[color_code[color_number]] == False:
        #         player = Player(user_name, password, color_code[color_number], playernum)
        #         return player
        #     else:
        #         print('this color is used! try again ...')
