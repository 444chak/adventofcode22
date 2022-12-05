input = []
with open("day4/input.txt") as f:
    for i in f:
        l = i.strip()
        left, right = l.split(',')
        l1, l2 = left.split('-')
        r1, r2 = right.split('-')
        input.append((int(l1), int(l2), int(r1), int(r2)))


def p1():
    asw= 0
    for i in input:
        if i[0] <= i[2] and i[1] >= i[3]: #if first range start before or at the same time of second AND end after or at the same time
            asw += 1
        elif i[2] <= i[0] and i[3] >= i[1]: # same for the other case
            asw += 1

    return asw
def p2():
    asw = 0 
    for i in input:
        if i[0] > i[3] or i[1] < i[2]: # if first range start after second or second start after first
            asw += 1

    return len(input)- asw 

print(p1(), p2())