from Player import Player


class Board:
    board_game = []

    def __init__(self):
        self.board_game = [None] * 24

    def add_player(self, un, pw, color, ID):
        player = Player(un, pw, color, ID)
        return player
