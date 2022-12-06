import argparse
from src.y2022 import day1, day2, day3, day4, day5, day6


DAY_MAP = {
    "22": {
        "1": day1,
        "2": day2,
        "3": day3,
        "4": day4,
        "5": day5,
        "6": day6
    }
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', help='AoC Year. Mapped to src/y<year>.')
    parser.add_argument('--day', help='Day of AoC year.')
    
    args = parser.parse_args()

    DAY_MAP[args.year][args.day].solve()

