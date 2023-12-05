import sys

FILE = r"2023-12-05-puzzle-input"
LINES = open(FILE, "r").read().split("\n\n")

seeds, *maps = LINES
seeds = list(map(int, seeds.split(": ")[1].split())) # seems we're doing this quite a lot

maps = [item.split(":")[1].strip().split("\n") for item in maps] # should be good at splitting things by end of AoC
maps = [[[int(num) for num in item.split()] for item in theMap] for theMap in maps]

def day5PartOne(seeds, maps):
    # fix this variable name later
    stupidVariableName = sys.maxsize

    for seed in seeds:
        # variable name (FIX LATER)
        theResult = seed

        for theMap in maps:

            for theRange in theMap:
                destinationRange, sourceRange, rangeDifference = theRange

                # From the reddit post
                if sourceRange <= theResult < sourceRange + rangeDifference:
                    theResult += (destinationRange - sourceRange)

                    break

        stupidVariableName = min(theResult, stupidVariableName)

    return stupidVariableName

if __name__ == "__main__":
    print(day5PartOne(seeds, maps)) # 173706076