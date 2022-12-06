from common.util import get_input, print_results
 

CONTENTS = get_input('day6')[0]


def find_packet_marker(stream, id_start, id_len):
    for idx, _ in enumerate(stream[id_start:]):
        if len(set(stream[idx-id_len:idx])) == id_len:
            return idx
    return 0

def part1(data):
    return find_packet_marker(data, 5, 4)


def part2(data):
    return find_packet_marker(data, 15, 14)


if __name__ == '__main__':
    print_results(part1(CONTENTS), part2(CONTENTS))

