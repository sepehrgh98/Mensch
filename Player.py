from color import *
import random
from gui import *


class Player:
    player_numbers = 0
    colors_in_use = {'red': False, 'blue': False, 'green': False, 'yellow': False}

    def __init__(self, username, password, color, playernum, game_frame, btn_list):
        self.btn_list = btn_list
        self.username = username
        self.password = password
        self.playernum = playernum
        self.color = color
        self.game_frame = game_frame
        self.player_pieces = [i for i in self.make_pieces()]
        Player.player_numbers += 1

    def check_user_pass(self):
        pass

    def __repr__(self):
        return f'Player {self.playernum} with color {self.color}'

    def __del__(self):
        self.player_numbers -= 1

    def player_color_class(self):
        if self.color == 'red':
            return Red
        elif self.color == 'blue':
            return Blue
        elif self.color == 'green':
            return Green
        else:
            return Yellow

    def make_pieces(self):
        if self.color == 'red':
            r1 = Red(1, self.btn_list[0])
            r2 = Red(2, self.btn_list[1])
            r3 = Red(3, self.btn_list[2])
            r4 = Red(4, self.btn_list[3])

            Player.colors_in_use['red'] = True
            return r1, r2, r3, r4

        elif self.color == 'blue':

            b1 = Blue(1, self.btn_list[0])
            b2 = Blue(2, self.btn_list[1])
            b3 = Blue(3, self.btn_list[2])
            b4 = Blue(4, self.btn_list[3])
            Player.colors_in_use['blue'] = True
            return b1, b2, b3, b4

        elif self.color == 'green':
            g1 = Green(1, self.btn_list[0])
            g2 = Green(2, self.btn_list[1])
            g3 = Green(3, self.btn_list[2])
            g4 = Green(4, self.btn_list[3])
            Player.colors_in_use['green'] = True
            return g1, g2, g3, g4

        elif self.color == 'yellow':
            y1 = Yellow(1, self.btn_list[0])
            y2 = Yellow(2, self.btn_list[1])
            y3 = Yellow(3, self.btn_list[2])
            y4 = Yellow(4, self.btn_list[3])
            Player.colors_in_use['yellow'] = True
            return y1, y2, y3, y4

    def Dice(self):
        return random.choice([1, 2, 3, 4, 5, 6])

    def Win(self):
        if len(self.player_pieces[0].winer_pieces) == 4:
            return True
        else:
            return False
