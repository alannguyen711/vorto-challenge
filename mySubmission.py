import sys
import math

def parse_input(path):
    loads = []
    with open(path, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.split()
            load_id = int(parts[0])
            pickup = tuple(map(float, parts[1].strip("()").split(',')))
            dropoff = tuple(map(float, parts[2].strip("()").split(',')))
            loads.append((load_id, pickup, dropoff))
    return loads

def main():
    path = sys.argv[1]
    loads = parse_input(path)
    print(path)

if __name__ == "__main__":
    main()
