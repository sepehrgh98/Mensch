from Player import Player


class Board:
    board_game = []

    def __init__(self):
        self.board_game = [None] * 24

    def add_player(self, un, pw, color, ID, game_frame, btn_list):
        player = Player(un, pw, color, ID, game_frame, btn_list)
        return player


