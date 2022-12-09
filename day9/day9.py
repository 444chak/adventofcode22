from math import sqrt

filename = 'day9/input.txt'
input = []
with open(filename) as f:
    for i in f:
        input.append(i.split())

def sqr(x):
    return x*x

def distance(x1, y1, x2, y2):
    return sqrt(sqr(y2-y1)+sqr(x2-x1))

def queue(xhead, yhead, xqueue, yqueue):
    if distance(xhead, yhead, xqueue, yqueue) == 0:
        return (0,0) # rien du tout
    if distance(xhead, yhead, xqueue, yqueue)/int(distance(xhead, yhead, xqueue, yqueue))==int(distance(xhead, yhead, xqueue, yqueue) and distance(xhead, yhead, xqueue, yqueue) >= 2):
        if yhead>yqueue and xhead == xqueue: # HAUT 
            return (0,1)
        if xhead < xqueue: # GAUCHE
            return (-1,0)
        if xhead > xqueue: # DROITE
            return (1,0)
        if yqueue > yhead: # BAS 
            return (0,-1)
    elif distance(xhead, yhead, xqueue, yqueue) >= 2:
        if not(yhead-yqueue<0): # HAUT 
            if xhead-xqueue<0: # GAUCHE
                return (-1,1)
            if not(xhead-xqueue<0): # DROITE
                return (1,1)
        if yhead-yqueue<0: # BAS 
            if xhead-xqueue<0: # GAUCHE
                return (-1,-1)
            if not(xhead-xqueue<0): # DROITE
                return (1,-1)
    return (0,0) # rien du tout

def horrificday(nodes):
    pos = [[0,0] for i in range(nodes)]
    passeds = [(0,0)]
    for i in input:
        for j in range(int(i[1])): # go 'j' times
            for node in range(1,nodes):
                if i[0] == 'R' and node==1: # go right
                    pos[node-1][0] += 1
                if i[0] == 'L'and node==1: # go left
                    pos[node-1][0] -= 1
                if i[0] == 'U'and node==1: # go up
                    pos[node-1][1] += 1
                if i[0] == 'D'and node==1: # go down
                    pos[node-1][1] -= 1
                pos[node][0], pos[node][1] = pos[node][0]+queue(pos[node-1][0], pos[node-1][1], pos[node][0], pos[node][1])[0], pos[node][1]+queue(pos[node-1][0], pos[node-1][1], pos[node][0], pos[node][1])[1]
                if node == nodes-1:
                    passeds.append((pos[node][0], pos[node][1]))

    return len(set(passeds))

print('part 1:',horrificday(2))
print('part 2:',horrificday(10))