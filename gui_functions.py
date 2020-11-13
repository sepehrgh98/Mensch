from tkinter import *
from Player import *




def add_players():
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
        self.Board.add_player()

    Login = Button(log_in_page, text="LOGIN", padx=123, command=login_clicked)
    Login.grid(row=3, column=0, columnspan=2, padx=(50, 0), pady=(10, 10), sticky="W")

