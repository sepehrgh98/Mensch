from game import *
from color import *
from Player import *

num = int(input('number of players:'))
print('----------------------------------------------------')
if num >= 2 and num <= 4:
    g1 = Game(num)

print('----------------------------------------------------')

for i in range(len(g1.Ranking)):
    if i == 0:
        print(f'1 - {g1.Ranking[i]}  King')
    else:
        print(f'{i+1} - {g1.Ranking[i]}')