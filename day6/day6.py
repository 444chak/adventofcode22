with open('day6/input.txt') as f:
    input = f.read()

def day6(input:str, nbdistinctchar:int):
    """
    How many characters need to be processed before the first start-of-message marker is detected

    Args:
        input (str): input
        nbdistinctchar (int): number of differents characters of the start-of-message marker

    Returns:
        int: index of start of message (after start-of-message marker)
    """
    for i in range(len(input)):
        for j in range(len(input[i:i+nbdistinctchar])):
            if len(list(filter(lambda a: a != input[i:i+nbdistinctchar][j], input[i:i+nbdistinctchar]))) != nbdistinctchar-1: # if lenght of list from which we remove all occurrences of j is not equal as nbdistinctchar-1
                break # change pattern 
            elif j == nbdistinctchar-1: # (if we dont change the pattern before and) if all characters of the pattern passeds the precedent condition 
                return i+nbdistinctchar 


print(f'Part one : {day6(input, 4)}')
print(f'Part two : {day6(input, 14)}')