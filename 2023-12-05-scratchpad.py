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

print('----------------------------------')
print('------------ PART ONE ------------')
print('----------------------------------')

print(day5PartOne(seeds, maps)) # 173706076 = correct

# print('----------------------------------')
# print('------------ PART TWO ------------')
# print('----------------------------------')


def onThe5thDayOfXmas(a,b,c,d):
    return not (b < c or d < a)

def day5PartTw0(seeds, maps):
    
    # thank you reddit tips
    redditRange = []

    for element in range(0, len(seeds), 2):
        redditRange.append((seeds[element], seeds[element] + seeds[element + 1] - 1))

    LINES.pop(0)

    for workingGroup in LINES:
        workingGroup = workingGroup.split("\n")
        values = workingGroup[1:]
        doppleGanger = seeds.copy()

        newRedditRange = []

        for fiveGoldenRings in values:
            d,s,r = fiveGoldenRings.split()
            d,s,r = int(d), int(s), int(r)

            for element in range(len(seeds)):

                if s <= seeds[element] < s+r:
                    doppleGanger[element] += d - s

            e = s + r - 1

            theNewNewRedditList = []

            for spread in redditRange:

                if onThe5thDayOfXmas(s, e, spread[0], spread[1]):
                    c1 = max(s,spread[0])
                    c2 = min(e,spread[1])
                    newRedditRange.append((c1 + d - s, c2 + d - s))

                    if spread[0] < c1:
                        theNewNewRedditList.append((spread[0],c1-1))

                    if spread[1] > c2:
                        theNewNewRedditList.append((c2+1,spread[1]))

                else:
                    theNewNewRedditList.append(spread)

            redditRange = theNewNewRedditList

        redditRange = newRedditRange + theNewNewRedditList

    print(min(redditRange)[0])

print('----------------------------------')
print('------------ PART TWO ------------')
print('----------------------------------')

day5PartTw0(seeds, maps)    # 11611182 = CORRECT - but the answer was derived by sneaky peaking the reddit tips
