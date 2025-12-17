# art.py
import sys
import random

chars = '\\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    # If the user provides numbers (e.g., python art.py 15 40)
    if len(sys.argv) == 3:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
    # If they just click Play (no numbers provided)
    else:
        print("No inputs found. Using defaults: 15 rows, 40 columns.")
        rows = 15
        cols = 40

    draw(rows, cols)