def openstack(file):
    """
    collect each stack of the file
    return : 
        dict of stacks
    """
    stacks = {
    }
    for i in range(1, 10):
        stacks[i] = []
    with open(file) as f:
        for line in f.readlines():
            if not (line.startswith("move")):
                for i in range(1, len(line),4):
                    if line[i] != ' ':
                        stacks[i//4+1].append(line[i])
                    
    for i in range(1,len(stacks)+1):
        stacks[i].reverse()
    return stacks


def part1(instructions):
    stacks = openstack('day5/input.txt')
    output = ''
    for i in instructions: # do rearrangements
        for j in range(1, i[0]+1):
            stacks[i[2]] += stacks[i[1]].pop()

    for i in stacks.values(): # collect top of each stack
        if len(i) > 0:
            output += str(i[-1])
    return output

def part2(instructions):
    stacks = openstack('day5/input.txt')
    output = ''
    for i in instructions: # do rearrangements
        stacks[i[2]] += stacks[i[1]][len(stacks[i[1]])-i[0]:]
        for j in range(1, i[0]+1):
            stacks[i[1]].pop()

    for i in stacks.values(): # collect top of each stack
        if len(i) > 0:
            output += str(i[-1])
    return output

# collect rearrangement instructions
with open(r'day5/input.txt') as f:
    input = []
    for line in f.readlines():
        if line.startswith("move"):
            input.append(line.strip())

intstr = [str(i) for i in range(10)]
instructions = []
for i in range(len(input)):
    a, b,c, d, e, f = input[i].split(' ')
    instructions.append([int(b), int(d), int(f)])

print(f'Part 1: {part1(instructions)}')
print(f'Part 2: {part2(instructions)}')