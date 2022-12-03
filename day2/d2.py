"""
X A Rock 1
Y B Paper 2
Z C Ciseau 3
Nul 3
Gagner 6
"""

with open('day2/input.txt') as f:
    tours = f.read()


tours = tours.replace(' ', '')
tours = tours.split('\n')

points = 0
valeurs = {
    'X':1,
    'Y':2,
    'Z':3
}
symboles = {
    'X':'A',
    'Y':'B',
    'Z':'C'
}

gagner = ['AY', 'CX', 'BZ']
for i in tours:
    points += valeurs[i[1]]
    if symboles[i[1]] == i[0]:
        points += 3
    elif i in gagner:
        points += 6


print(points)

from turtle import *
color ("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()