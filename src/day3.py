from util import get_puzzle_input_str


BAG_CONTENTS = [bag[0] for bag in get_puzzle_input_str('day3', '\n')]


def get_char_ord(ch):
    if ch.islower():
        return ord(ch) - 96
    return ord(ch) - 65 + 27

def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]


def part1(bags):
    total = 0
    for bag in bags:
        compartment_L, compartment_R = split(bag)
        # This works as there is only one common item per bag
        total += get_char_ord(''.join(set(compartment_L).intersection(compartment_R)))
    return total


def part2(bags):
    total = 0
    for i in range(0, len(bags), 3):
        group = bags[i:i+3]
        # This works as there is only one common item per bag
        total += get_char_ord(''.join(set(group[0]).intersection(set(group[1]), set(group[2]))))
    return total


if __name__ == '__main__':
    print(f'Part 1: {part1(BAG_CONTENTS)}')
    print(f'Part 2: {part2(BAG_CONTENTS)}')
