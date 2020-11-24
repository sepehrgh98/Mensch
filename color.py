
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
        self.color = 'red'

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
        self.color = 'blue'

    def __repr__(self):
        return f'b{self.number}'


class Green(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 18

    def __init__(self, number, btn_object):
        self.btn_object = btn_object
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.number = number
        self.color = 'green'

    def __repr__(self):
        return f'g{self.number}'


class Yellow(Color):
    save_pieces = []
    winer_pieces = []
    piece_position = None
    start_home = 12

    def __init__(self, number, btn_object):
        self.btn_object = btn_object
        self.save_pieces.append(self)
        self.piece_position = -1  # means my piece is in save list
        self.number = number
        self.color = 'yellow'

    def __repr__(self):
        return f'y{self.number}'
