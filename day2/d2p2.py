"""
A Rock 1
B Paper 2
C Ciseau 3
Nul 3
Gagner 6

X perdre
Y égalité
Z gagner
"""

with open('day2/input.txt') as f:
    tours = f.read()


tours = tours.replace(' ', '')
tours = tours.split('\n')

points = 0
valeurs = {
    'A':1,
    'B':2,
    'C':3
}

valeurs2 = {
    'X':1,
    'Y':2,
    'Z':3
}

symboles = {
    'A':'X',
    'B':'Y',
    'C':'Z'
}

gagner = {'A':'Y', 'C': 'X', 'B':'Z'}
gagner = {'A':'Y', 'C': 'X', 'B':'Z'}
for i in tours:
    if i[1] == 'Y':
        points += 3
        points += valeurs[i[0]]
    if i[1] == 'Z':
        points += 6
        points+= valeurs2[gagner[i[0]]]
    if i[1] == 'X':
        if i[0] == 'A': points += 3
        if i[0] == 'B': points += 1
        if i[0] == 'C': points += 2

    


print(points)