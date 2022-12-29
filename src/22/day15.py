from ..common.util import get_puzzle_input_str, print_results


CONTENTS = [line[0] for line in get_puzzle_input_str('22', 'day15', '\n')]


def parse(data):
    res = []
    for i in data:
        s, b = i.split(':')[0], i.split(':')[1]
        s, b = list(map(int, s.split('x=')[1].split(', y='))), list(map(int, b.split('x=')[1].split(', y=')))
        res.append({'sensor': s, 'beacon': b})
    return res


def radius(data):
    return abs(data['beacon'][0] - data['sensor'][0]) + abs(data['beacon'][1] - data['sensor'][1])


# Solution Part1
def part1(data, d):
    cov, beacons = set(), set()
    for elem in parse(data):
        r, dist = radius(elem), abs(elem['sensor'][1] - d)
        if dist > r:
            continue
        for i in range(elem['sensor'][0]-(r-dist), elem['sensor'][0]+(r-dist)+1):
            cov.add(i)
        if elem['beacon'][1] == d:
            beacons.add(elem['beacon'][0])
    return len(cov) - len(beacons)


# Solution Part2
def part2(data):
    return 0


def solve():
    print_results(part1(CONTENTS, 2000000), part2(CONTENTS))

