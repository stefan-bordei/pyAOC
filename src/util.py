
# Helper functions
def get_puzzle_input_num(day, separator='\n'):
    with open(f'./data/{day}.txt', 'r') as scanned_input:
        return [[int(item) for item in line.split('\n') if item] for line in scanned_input.read().split(separator) if line]

def get_puzzle_input_str(day, separator='\n'):
    with open(f'./data/{day}.txt', 'r') as scanned_input:
        return [[item for item in line.split('\n') if item] for line in scanned_input.read().split(separator) if line]

