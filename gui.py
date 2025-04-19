from tkinter import *
from PIL import ImageTk, Image
from color import *
from Board import Board
from game import Game
from game_history import *
from tkinter import messagebox


class Gui:
    enable_colors = ['red', 'blue', 'green', 'yellow']
    dice_btn = 0
    dice_number = None
    counter = 0
    T_index = -1
    turn_gui = None
    panel = None
    moveable_pieces = {}
    board_game_btn = []
    red_home_btn = []
    blue_home_btn = []
    green_home_btn = []
    yellow_home_btn = []
    piece_choosed = []
    piece_in_game = {}
    home_dis = 0
    TURN = None
    win_btn = []
    label_text_1_color = ''

    def __init__(self):
        self.Bord = Board()
        self.Game = Game(self.Bord)
        self.file = 0
        self.root = Tk()
        self.root.title("Mench")
        self.root.configure(background='#FFCA7A')
        self.root.geometry('1005x733')
        self.root.iconbitmap('E:/Maktab/Mench/images/logo.ico')
        self.root.resizable(0, 0)
        self.myroot = self.root
        self.make_items()

    def check_user_pass(self, myuser, mypass):
        mydataBase = {}
        with open("./DATABASE.txt", 'r') as database:
            for line in database:
                line = line.rstrip('\n')
                line = line.replace(' ', ',', 1)
                line = line.replace(' ', '')
                user_pass = line.split(',')
                mydataBase[user_pass[0]] = user_pass[1]

        database_usr= mydataBase.keys()
        if myuser in database_usr:
            if mydataBase[myuser] == mypass:
                print(f'WELCOME {myuser}')
                return True
            else:
                print('INCORRECT PASSWORD!')
                return 'INCORRECT PASSWORD!'
        else:
            print("this user Has not registered!")
            return "this user Has not registered!"

    def make_items(self):
        # MENU BAR
        global menubar
        menubar = Menu(self.root)
        self.file = Menu(menubar, tearoff=0, bg='#FFCA7A')
        self.file.add_command(label="Add Player", command=self.add_players_gui)
        self.file.add_separator()
        self.file.add_command(label="Start Game", command=lambda: self.start_game())
        self.file.add_separator()
        self.file.add_command(label="New Game", command=lambda: self.new_game())
        self.file.add_separator()
        self.file.add_command(label="Exit", command=lambda: self.exit(self.root))
        self.root.config(menu=menubar)
        menubar.add_cascade(label="Game", menu=self.file)

        self.file.entryconfig("Start Game", state="disable")

        # DEFINE FRAMES
        player_frame = LabelFrame(self.root, background="#F56038")
        player_frame.grid(row=1, column=0, sticky=W, ipadx=40, ipady=36, padx=(10, 3), pady=(5, 3))
        global dice_frame
        dice_frame = LabelFrame(self.root, background="#FFA325")
        dice_frame.grid(row=2, column=0, sticky=W, ipadx=38, ipady=12, padx=(10, 3), pady=(3, 3))
        global game_frame
        game_frame = LabelFrame(self.root, background="#0A2F35")
        game_frame.grid(row=1, column=1, rowspan=2, pady=(5, 0))

        # PLAYER_FRAME
        player_lab = Label(player_frame, bg="#F56038", text="Players", font=("Times", "20", "bold italic"))
        player_lab.grid(row=0, column=0, ipadx=7, padx=(50, 0), pady=(10, 3))

        global player_1, player_2, player_3, player_4
        player_1 = Label(player_frame, bg="#F56038", font=("Times", "15", "bold italic"))
        player_1.grid(row=1, column=0, pady=(30, 3), sticky=W)

        player_2 = Label(player_frame, bg="#F56038", font=("Times", "15", "bold italic"))
        player_2.grid(row=2, column=0, pady=(5, 3), sticky=W)

        player_3 = Label(player_frame, bg="#F56038", font=("Times", "15", "bold italic"))
        player_3.grid(row=3, column=0, pady=(5, 3), sticky=W)

        player_4 = Label(player_frame, bg="#F56038", font=("Times", "15", "bold italic"))
        player_4.grid(row=4, column=0, pady=(5, 3), sticky=W)

        # DICE_FRAME

        global dice_lab
        self.turn_gui = StringVar()
        self.turn_gui.set('')
        dice_lab = Label(dice_frame, bg="#FFA325", textvariable=self.turn_gui, font=("Helvetica", "12", "bold italic"))
        dice_lab.grid(row=0, column=0, padx=(50, 0), pady=(10, 60))
        self.dice_number = IntVar()
        self.dice_number.set(0)
        dice_number = Label(dice_frame, bg="#FFA325", textvariable=self.dice_number,
                            font=("Helvetica", "12", "bold italic"))
        dice_number.grid(row=3, column=0, padx=(65, 0), pady=(10, 60))

        self.dice_btn = Button(dice_frame, bg="#FFA329", text='Roll Dice...', font=("Helvetica", "12", "bold italic"),
                               state='disabled',
                               command=lambda: self.dice_clicked())
        self.dice_btn.grid(row=1, column=0, padx=(65, 0), pady=(10, 10))

        img = Image.open("./images/no_dice.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel = Label(dice_frame, bg='#FFA325', image=img)
        self.panel.image = img
        self.panel.grid(row=2, column=0, padx=(65, 0), pady=(60, 10))

        # GAME_FRAME
        # IMAGES

        borR = Image.open('./images/redcircle.png')
        borR = borR.resize((60, 55), Image.ANTIALIAS)
        im1 = ImageTk.PhotoImage(borR)

        borB = Image.open('./images/bluecircle.png')
        borB = borB.resize((60, 55), Image.ANTIALIAS)
        im2 = ImageTk.PhotoImage(borB)

        borG = Image.open('./images/greencircle.png')
        borG = borG.resize((60, 55), Image.ANTIALIAS)
        im3 = ImageTk.PhotoImage(borG)

        borY = Image.open('./images/yellowcircle.png')
        borY = borY.resize((60, 55), Image.ANTIALIAS)
        im4 = ImageTk.PhotoImage(borY)

        borW = Image.open('./images/boardcircle.png')
        borW = borW.resize((60, 55), Image.ANTIALIAS)
        im5 = ImageTk.PhotoImage(borW)

        red_home_1 = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        red_home_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        self.red_home_btn.append(red_home_1)
        red_home_2 = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        red_home_2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
        self.red_home_btn.append(red_home_2)
        red_home_3 = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        red_home_3.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
        self.red_home_btn.append(red_home_3)
        red_home_4 = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        red_home_4.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))
        self.red_home_btn.append(red_home_4)

        green_home_1 = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        green_home_1.grid(row=0, column=7, padx=(10, 10), pady=(10, 10))
        self.green_home_btn.append(green_home_1)
        green_home_2 = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        green_home_2.grid(row=0, column=8, padx=(10, 10), pady=(10, 10))
        self.green_home_btn.append(green_home_2)
        green_home_3 = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        green_home_3.grid(row=1, column=7, padx=(10, 10), pady=(10, 10))
        self.green_home_btn.append(green_home_3)
        green_home_4 = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        green_home_4.grid(row=1, column=8, padx=(10, 10), pady=(10, 10))
        self.green_home_btn.append(green_home_4)

        blue_home_1 = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        blue_home_1.grid(row=7, column=0, padx=(10, 10), pady=(10, 10))
        self.blue_home_btn.append(blue_home_1)
        blue_home_2 = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        blue_home_2.grid(row=7, column=1, padx=(10, 10), pady=(10, 10))
        self.blue_home_btn.append(blue_home_2)
        blue_home_3 = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        blue_home_3.grid(row=8, column=0, padx=(10, 10), pady=(10, 10))
        self.blue_home_btn.append(blue_home_3)
        blue_home_4 = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        blue_home_4.grid(row=8, column=1, padx=(10, 10), pady=(10, 10))
        self.blue_home_btn.append(blue_home_4)

        yellow_home_1 = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        yellow_home_1.grid(row=7, column=7, padx=(10, 10), pady=(10, 10))
        self.yellow_home_btn.append(yellow_home_1)
        yellow_home_2 = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        yellow_home_2.grid(row=7, column=8, padx=(10, 10), pady=(10, 10))
        self.yellow_home_btn.append(yellow_home_2)
        yellow_home_3 = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        yellow_home_3.grid(row=8, column=7, padx=(10, 10), pady=(10, 10))
        self.yellow_home_btn.append(yellow_home_3)
        yellow_home_4 = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0)
        yellow_home_4.grid(row=8, column=8, padx=(10, 10), pady=(10, 10))
        self.yellow_home_btn.append(yellow_home_4)

        btn_1 = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(1))
        btn_1.image = im1
        btn_1.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_1)

        btn_2 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(2))
        btn_2.image = im5
        btn_2.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_2)

        btn_3 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(3))
        btn_3.grid(row=5, column=1, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_3)

        btn_4 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(4))
        btn_4.grid(row=5, column=2, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_4)

        btn_5 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(5))
        btn_5.grid(row=5, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_5)

        btn_6 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(6))
        btn_6.grid(row=6, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_6)

        btn_7 = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(7))
        btn_7.image = im2
        btn_7.grid(row=7, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_7)

        btn_8 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(8))
        btn_8.grid(row=7, column=4, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_8)

        btn_9 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                       command=lambda: self.board_clicked(9))
        btn_9.grid(row=7, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_9)

        btn_10 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(10))
        btn_10.grid(row=6, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_10)

        btn_11 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(11))
        btn_11.grid(row=5, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_11)

        btn_12 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(12))
        btn_12.grid(row=5, column=6, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_12)

        btn_13 = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(13))
        btn_13.image = im4
        btn_13.grid(row=5, column=7, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_13)

        btn_14 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(14))
        btn_14.grid(row=4, column=7, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_14)

        btn_15 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(15))
        btn_15.grid(row=3, column=7, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_15)

        btn_16 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(16))
        btn_16.grid(row=3, column=6, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_16)

        btn_17 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(17))
        btn_17.grid(row=3, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_17)

        btn_18 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(18))
        btn_18.grid(row=2, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_18)

        btn_19 = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(19))
        btn_19.image = im3
        btn_19.grid(row=1, column=5, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_19)

        btn_20 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(20))
        btn_20.grid(row=1, column=4, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_20)

        btn_21 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(21))
        btn_21.grid(row=1, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_21)

        btn_22 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(22))
        btn_22.grid(row=2, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_22)

        btn_23 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(23))
        btn_23.grid(row=3, column=3, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_23)

        btn_24 = Button(game_frame, image=im5, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                        command=lambda: self.board_clicked(24))
        btn_24.grid(row=3, column=2, padx=(10, 10), pady=(10, 10))
        self.board_game_btn.append(btn_24)

        self.red_win = Button(game_frame, image=im1, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                              command=lambda: self.win_clicked('red'))
        self.red_win.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
        self.win_btn.append(self.red_win)
        self.green_win = Button(game_frame, image=im3, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                                command=lambda: self.win_clicked('green'))
        self.green_win.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
        self.win_btn.append(self.green_win)
        self.blue_win = Button(game_frame, image=im2, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                               command=lambda: self.win_clicked('blue'))
        self.blue_win.grid(row=6, column=4, padx=(10, 10), pady=(10, 10))
        self.win_btn.append(self.blue_win)
        self.yellow_win = Button(game_frame, image=im4, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                                 command=lambda: self.win_clicked('yellow'))
        self.yellow_win.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))
        self.win_btn.append(self.yellow_win)

    def add_players_gui(self):
        log_in_page = Toplevel()
        log_in_page.configure(background='#FFCA7A')
        log_in_page.title("log in ")
        log_in_page.title("LOG IN")
        log_in_page.geometry('400x250')

        uname = Label(log_in_page, bg='#FFCA7A', text="Username:")
        uname.grid(row=0, padx=(50, 0), pady=(60, 10), sticky="W")
        passwd = Label(log_in_page, bg='#FFCA7A', text="Password:")
        passwd.grid(row=1, padx=(50, 0), pady=(10, 10), sticky="W")
        color = Label(log_in_page, bg='#FFCA7A', text="Color:")
        color.grid(row=2, padx=(50, 0), pady=(10, 10), sticky="W")

        un = StringVar()
        u1 = Entry(log_in_page, bg='#F08A5D', textvariable=un, width=35)
        u1.grid(row=0, column=1, padx=(10, 0), pady=(60, 5))


        pw = StringVar()
        u2 = Entry(log_in_page, bg='#F08A5D', textvariable=pw, width=35)
        u2.grid(row=1, column=1, padx=(10, 0))

        color_clicked = StringVar()
        color_clicked.set(self.enable_colors[0])

        drop = OptionMenu(log_in_page, color_clicked, *self.enable_colors)
        drop.config(width=29)
        drop.config(bg="#F08A5D")
        drop['menu'].config(bg='#F08A5D')
        drop.grid(row=2, column=1, padx=(10, 0))

        Login = Button(log_in_page, bg='#F08A5D', text="LOGIN", padx=123,
                       command=lambda: self.login_clicked(un.get(), pw.get(), color_clicked.get(), log_in_page, Login))
        Login.grid(row=3, column=0, columnspan=2, padx=(50, 0), pady=(10, 10), sticky="W")

    def login_clicked(self, username, password, mycolor, page_name, log_btn):
        check = True
        check = self.check_user_pass(username, password)
        if check == True:
            ID = 5 - len(self.enable_colors)
            if mycolor == 'red':
                borR = Image.open('./images/red.png')
                borR = borR.resize((40, 43), Image.ANTIALIAS)
                red = ImageTk.PhotoImage(borR)
                r1 = Button(game_frame, image=red, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(1, mycolor))
                r1.image = red
                r1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
                r2 = Button(game_frame, image=red, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(2, mycolor))
                r2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
                r3 = Button(game_frame, image=red, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(3, mycolor))
                r3.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
                r4 = Button(game_frame, image=red, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(4, mycolor))
                r4.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))
                self.piece_in_game[mycolor] = [r1, r2, r3, r4]
                self.Game.players.append(
                    self.Bord.add_player(username, password, mycolor, ID, game_frame, [r1, r2, r3, r4]))
            elif mycolor == 'blue':
                borB = Image.open('./images/blue.png')
                borB = borB.resize((40, 43), Image.ANTIALIAS)
                blue = ImageTk.PhotoImage(borB)
                b1 = Button(game_frame, image=blue, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(1, mycolor))
                b1.image = blue
                b1.grid(row=7, column=0, padx=(10, 10), pady=(10, 10))
                b2 = Button(game_frame, image=blue, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(2, mycolor))
                b2.grid(row=7, column=1, padx=(10, 10), pady=(10, 10))
                b3 = Button(game_frame, image=blue, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(3, mycolor))
                b3.grid(row=8, column=0, padx=(10, 10), pady=(10, 10))
                b4 = Button(game_frame, image=blue, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(4, mycolor))
                b4.grid(row=8, column=1, padx=(10, 10), pady=(10, 10))
                self.piece_in_game[mycolor] = [b1, b2, b3, b4]
                self.Game.players.append(
                    self.Bord.add_player(username, password, mycolor, ID, game_frame, [b1, b2, b3, b4]))

            elif mycolor == 'green':
                borG = Image.open('./images/green.png')
                borG = borG.resize((40, 43), Image.ANTIALIAS)
                green = ImageTk.PhotoImage(borG)
                g1 = Button(game_frame, image=green, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(1, mycolor))
                g1.image = green
                g1.grid(row=0, column=7, padx=(10, 10), pady=(10, 10))
                g2 = Button(game_frame, image=green, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(2, mycolor))
                g2.grid(row=0, column=8, padx=(10, 10), pady=(10, 10))
                g3 = Button(game_frame, image=green, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(3, mycolor))
                g3.grid(row=1, column=7, padx=(10, 10), pady=(10, 10))
                g4 = Button(game_frame, image=green, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(4, mycolor))
                g4.grid(row=1, column=8, padx=(10, 10), pady=(10, 10))
                self.piece_in_game[mycolor] = [g1, g2, g3, g4]
                self.Game.players.append(
                    self.Bord.add_player(username, password, mycolor, ID, game_frame, [g1, g2, g3, g4]))
            else:
                borY = Image.open('./images/yellow.png')
                borY = borY.resize((40, 43), Image.ANTIALIAS)
                yellow = ImageTk.PhotoImage(borY)
                y1 = Button(game_frame, image=yellow, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(1, mycolor))
                y1.image = yellow
                y1.grid(row=7, column=7, padx=(10, 10), pady=(10, 10))
                y2 = Button(game_frame, image=yellow, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(2, mycolor))
                y2.grid(row=7, column=8, padx=(10, 10), pady=(10, 10))
                y3 = Button(game_frame, image=yellow, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(3, mycolor))
                y3.grid(row=8, column=7, padx=(10, 10), pady=(10, 10))
                y4 = Button(game_frame, image=yellow, bg="#0A2F35", padx=18, pady=10, borderwidth=0,
                            command=lambda: self.distanation(4, mycolor))
                y4.grid(row=8, column=8, padx=(10, 10), pady=(10, 10))
                self.piece_in_game[mycolor] = [y1, y2, y3, y4]
                self.Game.players.append(
                    self.Bord.add_player(username, password, mycolor, ID, game_frame, [y1, y2, y3, y4]))

            self.enable_colors.remove(mycolor)
            if ID == 1:
                player_1['text'] = f"1 - {username}"
                player_1['fg'] = mycolor
            elif ID == 2:
                player_2['text'] = f"2 - {username}"
                player_2['fg'] = mycolor
            elif ID == 3:
                player_3['text'] = f"3 - {username}"
                player_3['fg'] = mycolor
            else:
                player_4['text'] = f"4 - {username}"
                player_4['fg'] = mycolor

            page_name.destroy()

            if len(self.enable_colors) == 0:
                self.file.entryconfig("Add Player", state="disabled")

            if len(self.Game.players) >= 2 and len(self.Game.players) <= 4:
                self.file.entryconfig("Start Game", state="normal")
        else:
            messagebox.showerror("Error", check)
            page_name.destroy()


    def start_game(self):
        self.file.entryconfig("Add Player", state="disabled")
        self.Game.Turn = self.Game.referesh_turn()
        self.change_turn()
        self.dice_btn["state"] = NORMAL
        self.file.entryconfig("Start Game", state="disable")


    def dice_clicked(self):
        for i in self.board_game_btn:
            if i["bg"] == ['DarkGoldenRod']:
                i["bg"] = ['#0A2F35']
        self.Game.dice_number = self.Game.player_now.Dice()
        self.dice_number.set(self.Game.dice_number)
        print(f'dice = {self.Game.dice_number}')
        self.update_dice(self.Game.dice_number)
        self.dice_checker()

    def change_turn(self):
        try:
            self.T_index += 1
            self.T_index = self.T_index % (len(self.Game.Turn))
            self.TURN = self.Game.Turn[self.T_index]
            self.turn_gui.set(f'Turn : {self.TURN}')
            print('-----------------------------------------------------')
            print(f'Turn : {self.TURN}')
            for i in self.Game.players:
                if i.color == self.TURN:
                    self.Game.player_now = i
            self.dice_btn["state"] = NORMAL
        except ZeroDivisionError:
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('#######################################################')
            print('TURN LIST IS EMPTY...')
            print('...GAME FINISHED SUCCESSFULLY!')
            print('#######################################################')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    def update_dice(self, dice_num):
        self.panel = None
        if dice_num == 1:
            img = Image.open("./images/one.png")
        elif dice_num == 2:
            img = Image.open("./images/two.png")
        elif dice_num == 3:
            img = Image.open("./images/three.png")
        elif dice_num == 4:
            img = Image.open("./images/four.png")
        elif dice_num == 5:
            img = Image.open("./images/five.png")
        else:
            img = Image.open("./images/six.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(dice_frame, bg='#FFA325', image=img)
        panel.image = img
        panel.grid(row=2, column=0, padx=(65, 0), pady=(60, 10))

    def distanation(self, num, mycolor):

        mykey = self.moveable_pieces.keys()
        mypiece = 0
        for i in mykey:
            if i.number == num:
                mypiece = i
                self.piece_choosed.append(i)

        for i in self.board_game_btn:
            a = i
            if a['bg'] == 'DarkGoldenRod':
                a['bg'] = '#0A2F35'

        try:
            if self.piece_choosed[-1].color == mycolor:
                for i in self.piece_in_game[mycolor]:
                    if i["relief"] == 'sunken':
                        i["relief"] = ['raised']

                self.piece_choosed.append(mypiece)
                self.home_dis = self.moveable_pieces[mypiece]
                if self.home_dis[1] == 100:
                    if mypiece.__class__ == Red:
                        self.red_win["bg"] = ['DarkGoldenRod']
                    elif mypiece.__class__ == Blue:
                        self.blue_win["bg"] = ['DarkGoldenRod']
                    elif mypiece.__class__ == Green:
                        self.green_win["bg"] = ['DarkGoldenRod']
                    else:
                        self.yellow_win["bg"] = ['DarkGoldenRod']
                else:
                    self.board_game_btn[self.home_dis[1]]["bg"] = ['DarkGoldenRod']

                self.piece_choosed[-1].btn_object["relief"] = ['sunken']
        except KeyError:
            print('##################################################')
            print('...INVALID PIECE CLICKED!')
            print('##################################################')


    def board_clicked(self, num):
        flag = False
        for i in self.board_game_btn:
            a = i
            if a['bg'] == 'DarkGoldenRod':
                flag = True
        if flag:
            try:
                Dis = self.Game.move(self.piece_choosed[-1], self.home_dis[1], self.dice_number.get())
                self.board_game_btn[num - 1]["bg"] = "#0A2F35"
                myrow = self.board_game_btn[Dis].grid_info()['row']
                mycolumn = self.board_game_btn[Dis].grid_info()['column']
                mypadx = self.board_game_btn[Dis].grid_info()['padx']
                mypady = self.board_game_btn[Dis].grid_info()['pady']
            except IndexError:
                print('##################################################')
                print('...INVALID BUTTON CLICKED!')
                print('##################################################')


            li = list(self.piece_in_game.keys())
            try:
                for i in li:
                    if i != self.TURN:
                        for btn in self.piece_in_game[i]:
                            if btn.grid_info()['row'] == myrow and btn.grid_info()['column'] == mycolumn:
                                if i == 'red':
                                    r = self.red_home_btn[0].grid_info()['row']
                                    c = self.red_home_btn[0].grid_info()['column']
                                    btn.grid(row=r, column=c)
                                elif i == 'blue':
                                    r = self.blue_home_btn[0].grid_info()['row']
                                    c = self.blue_home_btn[0].grid_info()['column']
                                    btn.grid(row=r, column=c)
                                elif i == 'green':
                                    r = self.green_home_btn[0].grid_info()['row']
                                    c = self.green_home_btn[0].grid_info()['column']
                                    btn.grid(row=r, column=c)
                                else:
                                    r = self.yellow_home_btn[0].grid_info()['row']
                                    c = self.yellow_home_btn[0].grid_info()['column']
                                    btn.grid(row=r, column=c)

            except UnboundLocalError:
                print('##################################################')
                print('...INVALID BUTTON CLICKED!')
                print('##################################################')
            try:
                for i in self.piece_in_game[self.TURN]:
                    if i["relief"] == 'sunken':
                        i.grid(row=myrow, column=mycolumn, padx=mypadx, pady=mypady)
                        i["relief"] = ['raised']

                for i in self.piece_in_game[self.TURN]:
                    i["borderwidth"] = None
                    i["relief"] = ['raised']

            except KeyError:
                print('##################################################')
                print('...NO PLAYER ADDED!')
                print('##################################################')


            if self.Game.dice_number == 6:
                self.dice_btn["state"] = DISABLED
                img = Image.open("./images/w.png")
                img = img.resize((50, 50), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = Label(dice_frame, bg='#FFA325', image=img)
                panel.image = img
                panel.grid(row=2, column=0, padx=(65, 0), pady=(60, 10))

                reward = Toplevel()
                reward.configure(background='#FFCA7A')
                reward.title("REWARD!")
                reward.geometry('320x120')

                uname = Label(reward, bg='#FFCA7A', text='Wooow  6 !\n Roll again! this is your reward :)',
                              font=("Helvetica", "11", "bold italic"), anchor='w')
                uname.grid(row=0, column=1, padx=(0, 0), pady=(13, 10))

                img1 = Image.open("./images/reward.png")
                img1 = img1.resize((50, 50), Image.ANTIALIAS)
                img1 = ImageTk.PhotoImage(img1)
                panel1 = Label(reward, bg='#FFCA7A', image=img1)
                panel1.image = img1
                panel1.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

                ok = Button(reward, bg='#F08A5D', text="OK", padx=50, command=lambda: self.exit(reward))
                ok.grid(row=1, column=0, columnspan=2, padx=(30, 0), pady=(10, 10))
            else:
                self.change_turn()
                img = Image.open("./images/w.png")
                img = img.resize((50, 50), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = Label(dice_frame, bg='#FFA325', image=img)
                panel.image = img
                panel.grid(row=2, column=0, padx=(65, 0), pady=(60, 10))

    def dice_checker(self):
        print(f'player now : {self.Game.player_now}')
        if self.Game.dice_number == 6 or self.Game.may_3_times(self.Game.player_now):
            self.dice_btn["state"] = DISABLED
            self.moveable_pieces = self.Game.piece_position_destination(self.Game.player_now, self.Game.dice_number)
            self.counter = 0
            print(self.moveable_pieces)
            if len(self.moveable_pieces) != 0:
                for i in self.moveable_pieces.keys():
                    i.btn_object["borderwidth"] = ['6']
                    i.btn_object["relief"] = ['ridge']
            else:
                self.change_turn()
        else:
            self.Game.dice_number = "Can't!"
            self.dice_number.set(self.Game.dice_number)
            print(f'dice = {self.Game.dice_number}')
            self.counter += 1

        if self.counter == 3:
            self.counter = 0
            self.dice_btn["state"] = DISABLED
            img = Image.open("./images/w.png")
            img = img.resize((50, 50), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.panel = Label(dice_frame, bg='#FFA325', image=img)
            self.panel.image = img
            self.panel.grid(row=2, column=0, padx=(65, 0), pady=(60, 10))
            self.change_turn()

            for i in self.Game.players:
                if i.color == self.TURN:
                    self.Game.player_now = i
            self.dice_btn["state"] = NORMAL

    def win_clicked(self, color):
        try:
            Dis = self.Game.move(self.piece_choosed[-1], self.home_dis[1], self.dice_number.get())
            if self.piece_choosed[-1].__class__ == Red:
                self.piece_choosed[-1].btn_object.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
                self.red_win["bg"] = ['#0A2F35']
                if len(self.piece_choosed[-1].winer_pieces) == 2:
                    img = Image.open("./images/2.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 3:
                    img = Image.open("./images/3.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 4:
                    img = Image.open("./images/4.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
            elif self.piece_choosed[-1].__class__ == Blue:
                self.piece_choosed[-1].btn_object.grid(row=6, column=4, padx=(10, 10), pady=(10, 10))
                self.blue_win["bg"] = ['#0A2F35']
                if len(self.piece_choosed[-1].winer_pieces) == 2:
                    img = Image.open("./images/2.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=6, column=4, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 3:
                    img = Image.open("./images/3.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=6, column=4, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 4:
                    img = Image.open("./images/4.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=6, column=4, padx=(10, 10), pady=(10, 10))
            elif self.piece_choosed[-1].__class__ == Green:
                self.piece_choosed[-1].btn_object.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
                self.green_win["bg"] = ['#0A2F35']
                if len(self.piece_choosed[-1].winer_pieces) == 2:
                    img = Image.open("./images/2.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 3:
                    img = Image.open("./images/3.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 4:
                    img = Image.open("./images/4.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
            else:
                self.piece_choosed[-1].btn_object.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))
                self.yellow_win["bg"] = ['#0A2F35']
                if len(self.piece_choosed[-1].winer_pieces) == 2:
                    img = Image.open("./images/2.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 3:
                    img = Image.open("./images/3.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))
                elif len(self.piece_choosed[-1].winer_pieces) == 4:
                    img = Image.open("./images/4.png")
                    img = img.resize((20, 20), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    mypanel = Label(game_frame, bg='#0A2F35', image=img)
                    mypanel.image = img
                    mypanel.grid(row=4, column=6, padx=(10, 10), pady=(10, 10))

            self.piece_in_game[color].remove(self.piece_choosed[-1].btn_object)
        except IndexError:
            print('##################################################')
            print('...INVALID BUTTON CLICKED!')
            print('##################################################')
        try:
            if self.Game.player_now.Win():
                self.Game.Ranking.append(self.Game.player_now)
                print(f'{self.Game.player_now} Win!')
                self.Game.Turn.remove(self.TURN)

            if len(self.Game.Ranking) == len(self.Game.players) and self.Game.player_now.Win:
                ranking_page = Toplevel()
                ranking_page.configure(background='#FFCA7A')
                ranking_page.title("RANKING")
                ranking_page.geometry('400x250')

                king = Image.open("./images/king.png")
                king = king.resize((40, 40), Image.ANTIALIAS)
                king = ImageTk.PhotoImage(king)
                panel = Label(ranking_page, bg='#FFCA7A', image=king)
                panel.image = king
                panel.grid(row=0, column=1, padx=(40, 0), pady=(10, 10))

                myrank = []
                for i in range(len(self.Game.Ranking)):
                    myrank.append(Label(ranking_page, bg='#FFCA7A', font=("Helvetica", "10", "bold italic"),
                                        text=f"{i + 1} - {self.Game.Ranking[i]}"))

                for i in range(len(myrank)):
                    myrank[i].grid(row=i, padx=(50, 0), pady=(10, 10), sticky="W")

                # log
                rank = ""
                for i in self.Game.Ranking:
                    rank = rank + " - " + i.username
                game_his = log_def(rank, "./game_history.log")
                game_his.info("...done!", exc_info=True)
        except AttributeError:
            print('##################################################')
            print('...NO PLAYER ADDED!')
            print('##################################################')



        self.change_turn()

    def exit(self, myroot):
        myroot.destroy()
        self.dice_btn["state"] = NORMAL

    def new_game(self):
        del self.Game
        del self.Bord
        self.enable_colors = ['red', 'blue', 'green', 'yellow']
        self.dice_btn = 0
        self.dice_number = None
        self.counter = 0
        self.T_index = -1
        self.turn_gui = None
        self.panel = None
        self.moveable_pieces = {}
        self.board_game_btn = []
        self.red_home_btn = []
        self.blue_home_btn = []
        self.green_home_btn = []
        self.yellow_home_btn = []
        self.piece_choosed = []
        self.piece_in_game = {}
        self.home_dis = 0
        self.TURN = None
        self.win_btn = []
        self.label_text_1_color = ''
        self.root.destroy()
        self.__init__()