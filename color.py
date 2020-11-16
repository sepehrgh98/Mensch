from gui import *
from tkinter import *


class Color:
    pass


class Red(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 0

    def __init__(self, number, btn_object):
        self.btn_object = btn_object
        self.save_pieces.append(self)
        self.number = number
        self.piece_position = -1



    def __repr__(self):
        return f'r{self.number}'


class Blue(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 6

    def __init__(self, number, btn_object):

        self.btn_object = btn_object

        self.save_pieces.append(self)
        self.piece_position = -1
        self.number = number

    def __repr__(self):
        return f'b{self.number}'


class Green(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 12

    def __init__(self, number, btn_object):
        self.btn_object = btn_object
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.btn_object.grid(row=0, column=6, padx=(10, 100), pady=(100, 10))
        self.number = number

    def __repr__(self):
        return f'g{self.number}'


class Yellow(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 18

    def __init__(self, number, btn_object):
        self.btn_object = btn_object
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.btn_object.grid(row=6, column=6, padx=(10, 100), pady=(10, 100))
        self.number = number

    def __repr__(self):
        return f'y{self.number}'
