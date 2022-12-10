filename = 'day10/input.txt'
ins = []
with open(filename) as f:
    for i in f:
        if len(i.split()) == 1:
            ins.append([i.split()[0]])
        else:
            ins.append((i.split()[0], int(i.split()[1])))


signal_s = 0 
cycle = 0
x = 1

crt = [[] for i in range(6)]
current_row = 0
for i in ins:
    for cc in range(len(i)):
        cycle += 1
        if len(crt[current_row]) in range(x - 1, x + 2):
            crt[current_row].append('#')
        else:
            crt[current_row].append('.')
        if len(crt[current_row]) == 40:
            current_row +=1
        if cycle in (20, 60, 100, 140, 180, 220):
            signal_s += cycle * x
    if len(i) == 2:
        x+= i[1]

print('Part 1:',signal_s)
print('Part 2:')
for i in crt:
    print()
    for j in i:
        print(j, end='')
