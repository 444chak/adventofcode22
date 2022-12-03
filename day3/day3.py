alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = alpha + alpha.upper()

# dict for priority id 
PRIO = {}

for i in range(len(alpha)):
    PRIO[i+1] = alpha[i]

PRIO = {v: k for k, v in PRIO.items()}



with open("day3/input.txt") as f:
    input = f.readlines()

for i in range(len(input)):
    input[i] = input[i].replace('\n', '')


def sumprio(l:list, prio:list):
    """
    Take all element of l and calculate (and return) sum of priority id of these
    """
    sumprio = 0
    for i in l:
        sumprio += prio[i]
    return sumprio

def part1():
    both = []

    # check if one line of input has odd lenght
    for i in range(len(input)):
        if len(input[i])%2 != 0:
            print(i, False)
    # Spoiler : no.

    for i in range(len(input)):
        for j in input[i][:(len(input[i])//2)]:   # check for all element of first part of line
            if j in input[i][(len(input[i])//2):]:# is in second part of line
                both.append(j)                    # and add it in 'both' list
                break                             # and stop search for avoid duplicates



    return sumprio(both, PRIO)


def part2():
    groups = []
    for i in range(0,len(input), 3):
        for j in input[i]:                          # check for all element of line
            if j in input[i+1] and j in input[i+2]: # is in line+1 AND line+2
                groups.append(j)                    # and add it in 'groups' list
                break                               # and stop search for avoid duplicates
    return sumprio(groups, PRIO)
