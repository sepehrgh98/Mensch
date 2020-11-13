from tkinter import *

root = Tk()
root.title("Mench")
root.geometry('820x570')

# DEFINE GAME BUTTON
Game_button = Button(root, text="Game", padx=20)
Game_button.grid(row=0, column=0, sticky=W, padx=10, pady=5)

#DEINE FRAMES
player_frame = LabelFrame(root, padx=70, pady=118)
dice_frame = LabelFrame(root, padx=75, pady=118)
game_frame = LabelFrame(root, padx=288, pady=250)

#PLAYER_FRAME
player_lab = Label(player_frame, text="Player").pack()


#DICE_FRAME
l1 = Label(dice_frame, text="dice").pack()

#DICE_FRAME
l2 = Label(game_frame, text="game").pack()


player_frame.grid(row=1, column=0, sticky=W, padx=(10, 3), pady=(0, 3))
dice_frame.grid(row=2, column=0, sticky=W, padx=(10, 3), pady=(0, 3))
game_frame.grid(row=1, column=1, rowspan=2)

root.mainloop()
