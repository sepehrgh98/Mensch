from Board import *
from gui import *
import time


class Game:
    Turn = ['red', 'blue', 'green', 'yellow']
    players = []
    Ranking = []
    player_now = None
    dice_number = None

    def __init__(self):

        self.myBoard = Board()
        self.gui = Gui(self.myBoard, self)
        self.gui.make_items()
        self.gui.root.mainloop()

    def piece_position_destination(self, myplayer, d):
        print(self.myBoard.board_game)
        piece_pos_des = {}
        for i in myplayer.player_pieces:
            board_number = i.piece_position + d + i.start_home
            if board_number >= 24:
                board_number = board_number - 24
            if i.piece_position == -1:
                if d == 6:
                    if self.myBoard.board_game[i.start_home].__class__ != i.__class__:
                        piece_pos_des[i] = [i.piece_position, i.start_home]
            else:
                if i.piece_position + d < 24:
                    if self.myBoard.board_game[board_number].__class__ != i.__class__:
                        piece_pos_des[i] = [
                            i.piece_position + i.start_home - 24 if i.piece_position + i.start_home >= 24 else i.piece_position + i.start_home,
                            board_number]
                elif i.piece_position + d == 24:
                    piece_pos_des[i] = [i.piece_position + i.start_home - 24 if i.piece_position + i.start_home >= 24 else i.piece_position + i.start_home , 100]
        return piece_pos_des

    def move(self, piece, Destination_B, dice_number):

        if piece.piece_position == -1:
            piece.piece_position = 0
            if self.myBoard.board_game[Destination_B] is not None:
                Destination_B = self.remove_piece(piece, Destination_B)

            self.myBoard.board_game[Destination_B] = piece
            piece.save_pieces.remove(piece)
            return Destination_B

        else:
            if piece.piece_position + dice_number < 24:
                if self.myBoard.board_game[Destination_B] is not None:
                    Destination_B = self.remove_piece(piece, Destination_B)

                M = piece.piece_position + piece.start_home - 24 if piece.piece_position + piece.start_home >= 24 else piece.piece_position + piece.start_home
                self.myBoard.board_game[M] = None
                piece.piece_position = piece.piece_position + dice_number
                self.myBoard.board_game[Destination_B] = piece
                print(f'mydis = {Destination_B}')
                return Destination_B
            elif piece.piece_position + dice_number == 24:
                M = piece.piece_position + piece.start_home - 24 if piece.piece_position + piece.start_home >= 24 else piece.piece_position + piece.start_home
                self.myBoard.board_game[M] = None
                piece.winer_pieces.append(piece)
                piece.piece_position = 100
                return 100
            else:
                print('Invalid Movement!')

    def remove_piece(self, piece, Destination_B):
        if self.myBoard.board_game[Destination_B].__class__ == piece.__class__:
            print("can't do that !")
            return piece.piece_position + piece.start_home
        else:
            del_p = self.myBoard.board_game[Destination_B]
            del_p.piece_position = -1
            del_p.save_pieces.append(del_p)
            return Destination_B

    def referesh_turn(self):
        new_turn = []
        for i in self.players:
            if i.color in self.Turn:
                new_turn.append(i.color)
        return new_turn

    def may_3_times(self, player):
        for i in self.myBoard.board_game:
            for j in player.player_pieces:
                if i == j:
                    return True
        return False

    def dicing(self, dice_btn):
        dice_btn["state"] = NORMAL
        self.gui.dice_number.get()
        time.sleep(120)
        print(self.gui.dice_number)

    def new_game(self):
        return Game()
