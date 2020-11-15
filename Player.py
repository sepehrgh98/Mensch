from color import *
import random
from tkinter import *
from tkinter.ttk import *
from gui import *


class Player:
    player_numbers = 0
    colors_in_use = {'red': False, 'blue': False, 'green': False, 'yellow': False}

    def __init__(self, username, password, color, playernum, game_frame):
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
            photo_r = PhotoImage(file = r"E:\Maktab\Mench\red.png")
            photoimage_r = photo_r.subsample(8, 10)
            r1 = Red(1, Button(self.game_frame, image=photoimage_r, padx=13, pady=6))
            r2 = Red(2, Button(self.game_frame, image=photoimage_r, padx=13, pady=6))
            r3 = Red(3, Button(self.game_frame, image=photoimage_r, padx=13, pady=6))
            r4 = Red(4, Button(self.game_frame, image=photoimage_r, padx=13, pady=6))
            Player.colors_in_use['red'] = True
            return r1, r2, r3, r4

        elif self.color == 'blue':
            photo_b = PhotoImage(file=r"E:\Maktab\Mench\blue.png")
            photoimage_b = photo_b.subsample(10, 10)
            b1 = Blue(1, Button(self.game_frame, image=photoimage_b, padx=13, pady=6))
            b2 = Blue(2, Button(self.game_frame, image=photoimage_b, padx=13, pady=6))
            b3 = Blue(3, Button(self.game_frame, image=photoimage_b, padx=13, pady=6))
            b4 = Blue(4, Button(self.game_frame, image=photoimage_b, padx=13, pady=6))
            Player.colors_in_use['blue'] = True
            return b1, b2, b3, b4

        elif self.color == 'green':
            photo_g = PhotoImage(file=r"E:\Maktab\Mench\green.png")
            photoimage_g = photo_g.subsample(7, 8)
            g1 = Green(1, Button(self.game_frame, image=photoimage_g, padx=13, pady=6))
            g2 = Green(2, Button(self.game_frame, image=photoimage_g, padx=13, pady=6))
            g3 = Green(3, Button(self.game_frame, image=photoimage_g, padx=13, pady=6))
            g4 = Green(4, Button(self.game_frame, image=photoimage_g, padx=13, pady=6))
            Player.colors_in_use['green'] = True
            return g1, g2, g3, g4

        elif self.color == 'yellow':
            photo_y = PhotoImage(file=r"E:\Maktab\Mench\yellow.png")
            photoimage_y = photo_y.subsample(8, 10)
            y1 = Yellow(1, Button(self.game_frame, image=photoimage_y, padx=13, pady=6))
            y2 = Yellow(2, Button(self.game_frame, image=photoimage_y, padx=13, pady=6))
            y3 = Yellow(3, Button(self.game_frame, image=photoimage_y, padx=13, pady=6))
            y4 = Yellow(4, Button(self.game_frame, image=photoimage_y, padx=13, pady=6))
            Player.colors_in_use['yellow'] = True
            return y1, y2, y3, y4


    def Dice(self):
        return random.choice([1, 2, 3, 4, 5, 6])

    def Win(self):
        if len(self.player_pieces[0].winer_pieces) == 4:
            return True
        else:
            return False