from common.util import get_puzzle_input_num, print_results
 

CONTENTS = [sum(meals) for meals in get_puzzle_input_num('day1', '\n\n')]
CONTENTS.sort()
        
def part1(data):
    return data[-1]


def part2(data):
    return sum(data[-3:])


if __name__ == '__main__':
    print_results(part1(CONTENTS), part2(CONTENTS))

