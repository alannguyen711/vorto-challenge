import sys
import math
import re

def minutesDriven(pickup, dropoff):
    dist = abs(pickup[0] - dropoff[0]) ** 2 + abs(pickup[1] - dropoff[1]) ** 2
    return math.sqrt(dist)

def parseInput(path):
    loads = []
    with open(path, 'r') as file:
        next(file)
        for line in file:
            parts = line.split()
            loadID = int(parts[0])
            pickup = tuple(map(float, re.findall(r'[-]?\d+\.\d+', parts[1])))
            dropoff = tuple(map(float, re.findall(r'[-]?\d+\.\d+', parts[2])))
            loads.append((loadID, pickup, dropoff))
    return loads

def greedy(loads):
    MAX_TIME = 720 
    depot = (0, 0)
    drivers = []
    remainingLoads = loads.copy()

    while remainingLoads:
        location = depot
        currTime = 0
        loadList = []

        while remainingLoads and currTime < MAX_TIME:
            next = None
            minDist = float('inf')
            for load in remainingLoads:
                pickupDist = minutesDriven(location, load[1])
                if pickupDist < minDist:
                    next, minDist = load, pickupDist

            if next:
                totalDist = minDist + minutesDriven(next[1], next[2]) + minutesDriven(next[2], depot)
                if currTime + totalDist <= MAX_TIME:
                    loadList.append(next[0])
                    remainingLoads.remove(next)
                    location = next[2] 
                    currTime += totalDist
                else:
                    break
        drivers.append(loadList)

    return drivers


def main():
    path = sys.argv[1]
    loads = parseInput(path)
    drivers = greedy(loads)

    for x in drivers:
        print(x)

if __name__ == "__main__":
    main()
