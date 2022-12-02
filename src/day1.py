from util import get_puzzle_input_num
 
def solve():
    contents = [sum(meals) for meals in get_puzzle_input_num('day1', '\n\n')]
    contents.sort()
        
    # Part 1
    print(f'Part1: {contents[-1]}')

    # Part 2
    print(f'Part2: {sum(contents[-3:])}')


if __name__ == '__main__':
    solve()

