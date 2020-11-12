class Color:
    pass


class Red(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 0

    def __init__(self, number):
        self.save_pieces.append(self)
        self.piece_position = -1 #means my piece is in save list
        self.number = number


    def __repr__(self):
        return f'r{self.number}'


class Blue(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 6

    def __init__(self, number):
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.number = number

    def __repr__(self):
        return f'b{self.number}'


class Green(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 12

    def __init__(self, number):
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.number = number

    def __repr__(self):
        return f'g{self.number}'


class Yellow(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 18

    def __init__(self, number):
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.number = number

    def __repr__(self):
        return f'y{self.number}'
