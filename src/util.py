
# Helper functions
def get_puzzle_input_num(day, separator=None):
    with open(f'./data/{day}.txt', 'r') as scanned_input:
        if separator:
            prep_input = scanned_input.read().split(separator)
        else:
            prep_input = scanned_input.read()
        return [[int(item) for item in line.split('\n') if item] for line in prep_input if line]

def get_puzzle_input_str(day, separator=None):
    with open(f'./data/{day}.txt', 'r') as scanned_input:
        if separator:
            prep_input = scanned_input.read().split(separator)
        else:
            prep_input = scanned_input.read()
        return [[item for item in line.split('\n') if item] for line in prep_input if line]

