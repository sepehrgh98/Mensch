from gui_functions import *
from tkinter import *
from game import*

class Gui:

    def __init__(self, Bord):
        self.Bord = Bord
        self.root = Tk()
        self.root.title("Mench")
        self.root.geometry('900x650')
        self.make_items()
        self.root.mainloop()
    def make_items(self):
        # MENU BAR
        menubar = Menu(self.root)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="Add Player", command=self.add_players_gui)
        file.add_separator()
        file.add_command(label="Start Game")
        file.add_separator()
        file.add_command(label="New Game")
        file.add_separator()
        file.add_command(label="Exit")
        self.root.config(menu=menubar)
        menubar.add_cascade(label="Game", menu=file)

        # DEFINE FRAMES
        player_frame = LabelFrame(self.root)
        player_frame.grid(row=1, column=0, sticky=W, ipadx=70, ipady=130, padx=(10, 3), pady=(5, 3))
        dice_frame = LabelFrame(self.root)
        dice_frame.grid(row=2, column=0, sticky=W, ipadx=75, ipady=130, padx=(10, 3), pady=(3, 3))
        game_frame = LabelFrame(self.root)
        game_frame.grid(row=1, column=1, rowspan=2, pady=(5, 0))
        # PLAYER_FRAME
        player_lab = Label(player_frame, text="Player").pack()

        # DICE_FRAME
        dice_lab = Label(dice_frame, text="dice").pack()

        # GMAE_FRAME

        red_home = Button(game_frame, bg="red", padx=13, pady=6)
        red_home.grid(row=0, column=0, padx=(100, 10), pady=(100, 10))
        green_home = Button(game_frame, bg="green", padx=13, pady=6)
        green_home.grid(row=0, column=6, padx=(10, 100), pady=(100, 10))
        blue_home = Button(game_frame, bg="blue", padx=13, pady=6)
        blue_home.grid(row=6, column=0, padx=(100, 10), pady=(10, 100))
        yellow_home = Button(game_frame, bg="yellow", padx=13, pady=6)
        yellow_home.grid(row=6, column=6, padx=(10, 100), pady=(10, 100))

        btn_1 = Button(game_frame, text="1", bg="red", padx=13, pady=6)
        btn_1.grid(row=2, column=0, padx=(100, 10), pady=(10, 10))
        btn_2 = Button(game_frame, text="2", padx=13, pady=6)
        btn_2.grid(row=3, column=0, padx=(100, 10), pady=(10, 10))
        btn_3 = Button(game_frame, text="3", padx=13, pady=6)
        btn_3.grid(row=4, column=0, padx=(100, 10), pady=(10, 10))
        btn_4 = Button(game_frame, text="4", padx=13, pady=6)
        btn_4.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))
        btn_5 = Button(game_frame, text="5", padx=13, pady=6)
        btn_5.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
        btn_6 = Button(game_frame, text="6", padx=13, pady=6)
        btn_6.grid(row=5, column=2, padx=(10, 10), pady=(10, 10))
        btn_7 = Button(game_frame, text="7", bg="blue", padx=13, pady=6)
        btn_7.grid(row=6, column=2, padx=(10, 10), pady=(10, 100))
        btn_8 = Button(game_frame, text="8", padx=13, pady=6)
        btn_8.grid(row=6, column=3, padx=(10, 10), pady=(10, 100))
        btn_9 = Button(game_frame, text="9", padx=13, pady=6)
        btn_9.grid(row=6, column=4, padx=(10, 10), pady=(10, 100))
        btn_10 = Button(game_frame, text="10", padx=13, pady=6)
        btn_10.grid(row=5, column=4, padx=(10, 10), pady=(10, 10))
        btn_11 = Button(game_frame, text="11", padx=13, pady=6)
        btn_11.grid(row=4, column=4, padx=(10, 10), pady=(10, 10))
        btn_12 = Button(game_frame, text="12", padx=13, pady=6)
        btn_12.grid(row=4, column=5, padx=(10, 10), pady=(10, 10))
        btn_13 = Button(game_frame, text="13", bg="yellow", padx=13, pady=6)
        btn_13.grid(row=4, column=6, padx=(10, 100), pady=(10, 10))
        btn_14 = Button(game_frame, text="14", padx=13, pady=6)
        btn_14.grid(row=3, column=6, padx=(10, 100), pady=(10, 10))
        btn_15 = Button(game_frame, text="15", padx=13, pady=6)
        btn_15.grid(row=2, column=6, padx=(10, 100), pady=(10, 10))
        btn_16 = Button(game_frame, text="16", padx=13, pady=6)
        btn_16.grid(row=2, column=5, padx=(10, 10), pady=(10, 10))
        btn_17 = Button(game_frame, text="17", padx=13, pady=6)
        btn_17.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
        btn_18 = Button(game_frame, text="18", padx=13, pady=6)
        btn_18.grid(row=1, column=4, padx=(10, 10), pady=(10, 10))
        btn_19 = Button(game_frame, text="19", bg="green", padx=13, pady=6)
        btn_19.grid(row=0, column=4, padx=(10, 10), pady=(100, 10))
        btn_20 = Button(game_frame, text="20", padx=13, pady=6)
        btn_20.grid(row=0, column=3, padx=(10, 10), pady=(100, 10))
        btn_21 = Button(game_frame, text="21", padx=13, pady=6)
        btn_21.grid(row=0, column=2, padx=(10, 10), pady=(100, 10))
        btn_22 = Button(game_frame, text="22", padx=13, pady=6)
        btn_22.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))
        btn_23 = Button(game_frame, text="23", padx=13, pady=6)
        btn_23.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))
        btn_24 = Button(game_frame, text="24", padx=13, pady=6)
        btn_24.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        red_win = Button(game_frame, bg="red", padx=13, pady=6)
        red_win.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))
        green_win = Button(game_frame, bg="green", padx=13, pady=6)
        green_win.grid(row=1, column=3, padx=(10, 10), pady=(10, 10))
        blue_win = Button(game_frame, bg="blue", padx=13, pady=6)
        blue_win.grid(row=5, column=3, padx=(10, 10), pady=(10, 10))
        yellow_win = Button(game_frame, bg="yellow", padx=13, pady=6)
        yellow_win.grid(row=3, column=5, padx=(10, 10), pady=(10, 10))

    def add_players_gui(self):
        log_in_page = Toplevel()
        log_in_page.title("log in ")
        log_in_page.title("LOG IN")
        log_in_page.geometry('400x250')

        uname = Label(log_in_page, text="Username:").grid(row=0, padx=(50, 0), pady=(60, 10), sticky="W")
        passwd = Label(log_in_page, text="Password:").grid(row=1, padx=(50, 0), pady=(10, 10), sticky="W")
        color = Label(log_in_page, text="Color:").grid(row=2, padx=(50, 0), pady=(10, 10), sticky="W")

        un = StringVar()
        u1 = Entry(log_in_page, textvariable=un, width=35).grid(row=0, column=1, padx=(10, 0), pady=(60, 5))

        pw = StringVar()
        u2 = Entry(log_in_page, textvariable=pw, width=35).grid(row=1, column=1, padx=(10, 0))

        enable_colors = []

        for col, status in Player.colors_in_use.items():
            if not status:
                enable_colors.append(col)
        color_clicked = StringVar()
        color_clicked.set(enable_colors[0])

        color_clicked = StringVar()

        drop = OptionMenu(log_in_page, color_clicked, *enable_colors)
        drop.config(width=29)
        drop.grid(row=2, column=1, padx=(10, 0))

        def login_clicked():
            global username
            username = un.get()
            global password
            password = pw.get()
            global mycolor
            mycolor = color_clicked.get()
            ID = len(enable_colors)-1
            Game.players.append(self.Bord.add_player(username, password, mycolor, ID))
            print(Game.players)


        Login = Button(log_in_page, text="LOGIN", padx=123, command=login_clicked)
        Login.grid(row=3, column=0, columnspan=2, padx=(50, 0), pady=(10, 10), sticky="W")
















