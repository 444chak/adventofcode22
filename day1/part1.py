
with open('day1/input.txt') as f:
    elfs = f.read()


elfs = elfs.split('\n')

elfs = str(elfs).replace('\'\'','|')
elfs = str(elfs).replace('\'','')
elfs = str(elfs).replace(' ','')
elfs = str(elfs).replace(',|,','|')
elfs = str(elfs).replace('[','')
elfs = str(elfs).replace(']','')
elfs = str(elfs).split('|')

for i in range(len(elfs)):
    elfs[i] = elfs[i].split(',')


meal = []

for i in elfs:
    sum = 0
    for j in i:
        sum += int(j)
    meal.append(sum)
    
trio = []
for i in range(3):
    trio.append(max(meal))
    meal.remove(max(meal))


toptrio = 0
for i in trio:
    toptrio += i

print(toptrio)