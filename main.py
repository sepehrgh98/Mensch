from game import *


g1 = Game()


for i in range(len(g1.Ranking)):
    if i == 0:
        print(f'1 - {g1.Ranking[i]}  King')
    else:
        print(f'{i+1} - {g1.Ranking[i]}')
