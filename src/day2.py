from util import get_puzzle_input_str
from enum import Enum


contents = get_puzzle_input_str('day2', '\n')

# Mappings
class SelectionWeight(Enum):
    X = 1
    Y = 2
    Z = 3

class LooseMatrix(Enum):
    A = 'Z'
    B = 'X'
    C = 'Y'

class WinMatrix(Enum):
    A = 'Y' 
    B = 'Z' 
    C = 'X'

class DrawMapping(Enum):
    A = 'X'
    B = 'Y'
    C = 'Z'

# Solution Part1
def part1():
    score = 0
    for game in contents:
        score += SelectionWeight[game[0][2]].value
        if WinMatrix[game[0][0]].value == game[0][2]:
            score += 6
        if DrawMapping[game[0][0]].value == game[0][2]:
            score += 3
    return score

# Solution Part2
def part2():
    score = 0
    for game in contents:
        if game[0][2] == 'X':
            score += SelectionWeight[LooseMatrix[game[0][0]].value].value
        if game[0][2] == 'Y':
            score += 3 + SelectionWeight[DrawMapping[game[0][0]].value].value
        if game[0][2] == 'Z':
            score += 6 + SelectionWeight[WinMatrix[game[0][0]].value].value
    return score
            


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')

