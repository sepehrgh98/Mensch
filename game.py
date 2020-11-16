from Board import *
from Player import *
from color import *
from gui import *
import time


class Game:
    Turn = ['red', 'blue', 'green', 'yellow']
    players = []
    Ranking = []
    player_now = None
    dice_number = None

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.myBoard = Board()
        self.gui = Gui(self.myBoard, self)
        self.gui.make_items()
        self.gui.root.mainloop()

    def piece_position_destination(self, myplayer, d):
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
                if i.piece_position + d <= 24:
                    if self.myBoard.board_game[board_number].__class__ != i.__class__:
                        piece_pos_des[i] = [
                            i.piece_position + i.start_home - 24 if i.piece_position + i.start_home >= 24 else i.piece_position + i.start_home,
                            board_number]
        return piece_pos_des

    def Start(self, turn_gui, dice_btn):
        self.Turn = self.referesh_turn()
        T_index = 0
        dice_number = 0
        while True:
            game_Turn = self.Turn[T_index]
            turn_gui.set(f'Turn : {game_Turn}')
            print('-----------------------------------------------------')
            print(f'Turn : {game_Turn}')
            for i in self.players:
                if i.color == game_Turn:
                    self.player_now = i
            self.dicing(dice_btn)
            break

            # if self.gui.dice_btn_flag:
            #     for _ in range(3):
            #         if self.gui.dice_btn_flag:
            #             dice_number = player_now.Dice()
            #             print(f'dice = {dice_number}')
            #             if dice_number == 6 or self.may_3_times(player_now):
            #                 break
            #         self.gui.dice_btn_flag = False



                # moveable_pieces = self.piece_position_destination(player_now, dice_number)
                # if len(moveable_pieces) != 0:
                #     print(moveable_pieces)
                #     p = int(input('choose the piece :')) - 1
                #     a = list(moveable_pieces.keys())
                #     li = moveable_pieces[a[p]]
                #     self.move(a[p], li[1], dice_number)
                #     print(self.myBoard.board_game)
                #     print(
                #         f'save list : {Red.save_pieces}      ,save list : {Blue.save_pieces}      ,save list : {Green.save_pieces}       ,save list : {Yellow.save_pieces}')
                #     print(
                #         f'winner list : {Red.winer_pieces}     ,winner list : {Blue.winer_pieces}     ,winner list : {Green.winer_pieces}   ,winner list : {Yellow.winer_pieces}')
                # if player_now.Win():
                #     self.Turn.remove(game_Turn)
                #     self.Ranking.append(player_now)
            #----------------------------------------------------------------------------------
                # for i in self.players:
                #     if i.color == game_Turn:
                #         for _ in range(3):
                #             dice_number = i.Dice()
                #             print(f'dice = {dice_number}')
                #             if dice_number == 6 or self.may_3_times(i):
                #                 break
                #         moveable_pieces = self.piece_position_destination(i, dice_number)
                #         if len(moveable_pieces) != 0:
                #             print(moveable_pieces)
                #             p = int(input('choose the piece :')) - 1
                #             a = list(moveable_pieces.keys())
                #             li = moveable_pieces[a[p]]
                #             self.move(a[p], li[1], dice_number)
                #             print(self.myBoard.board_game)
                #             print(f'save list : {Red.save_pieces}      ,save list : {Blue.save_pieces}      ,save list : {Green.save_pieces}       ,save list : {Yellow.save_pieces}')
                #             print(f'winner list : {Red.winer_pieces}     ,winner list : {Blue.winer_pieces}     ,winner list : {Green.winer_pieces}   ,winner list : {Yellow.winer_pieces}')
                #         if i.Win():
                #             self.Turn.remove(game_Turn)
                #             self.Ranking.append(i)
                # if len(self.Turn) == 0:
                #     break
                # if dice_number != 6:
                #     T_index += 1
                # T_index = T_index % (len(self.Turn))

    def move(self, piece, Destination_B, dice_number):
        if piece.piece_position == -1:
            piece.piece_position = 0
            if self.myBoard.board_game[Destination_B] != None:
                Destination_B = self.remove_piece(piece, Destination_B)

            self.myBoard.board_game[Destination_B] = piece
            piece.save_pieces.remove(piece)
            return Destination_B

        else:
            if piece.piece_position + dice_number < 24:
                if self.myBoard.board_game[Destination_B] != None:
                    Destination_B = self.remove_piece(piece, Destination_B)

                M = piece.piece_position + piece.start_home - 24 if piece.piece_position + piece.start_home >= 24 else piece.piece_position + piece.start_home
                self.myBoard.board_game[M] = None
                piece.piece_position = piece.piece_position + dice_number
                self.myBoard.board_game[Destination_B] = piece
            elif piece.piece_position + dice_number == 24:
                M = piece.piece_position + piece.start_home - 24 if piece.piece_position + piece.start_home >= 24 else piece.piece_position + piece.start_home
                self.myBoard.board_game[M] = None
                piece.winer_pieces.append(piece)
                piece.piece_position = 100
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

    def win(self, piece):
        pass
