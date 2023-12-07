from collections import Counter # store different objects and provide a way to access the contained objects and iterate over them
from functools import cmp_to_key # each element is compared with every other element of the list until a sorted list is obtained

FILE = r"2023-12-07-puzzle-input"

LINES = [line.strip().split() for line in open(FILE, "r").readlines()]
LINES = list(map(lambda x: [x[0], int(x[1])], LINES))

cardValuesP1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
# initial values were normal, but in part 2, we are changing the order (Jack is now a Joker)
cardValuesP2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def cardsDealt(theCards):
    score = Counter(theCards)
    measureOfRepitition = score.most_common()
    if measureOfRepitition[0][1] == 5:
        return 6
    if measureOfRepitition[0][1] == 4:
        return 5
    if measureOfRepitition[0][1] == 3:
        if measureOfRepitition[1][1] == 2:
            return 4
        return 3
    if measureOfRepitition[0][1] == 2:
        if measureOfRepitition[1][1] == 2:
            return 2
        return 1
    return 0

def cardsDealtWeight(theCards):
    compareHands = Counter(theCards)
    joker = compareHands["J"]
    del compareHands["J"]
    measureOfRepitition = compareHands.most_common()
    if len(measureOfRepitition) < 2:
        return 6
    if measureOfRepitition[0][1] + joker == 5:
        return 6
    if measureOfRepitition[0][1] + joker == 4:
        return 5
    if (measureOfRepitition[0][1] + joker == 3 and measureOfRepitition[1][1] == 2) or (measureOfRepitition[0][1] == 3 and measureOfRepitition[1][1] + joker == 2):
        return 4
    if measureOfRepitition[0][1] + joker == 3:
        return 3
    if (measureOfRepitition[0][1] + joker == 2 and measureOfRepitition[1][1] == 2) or (measureOfRepitition[0][1] == 2 and measureOfRepitition[1][1] + joker == 2):
        return 2
    if measureOfRepitition[0][1] + joker == 2:
        return 1
    return 0

def compare(firstCard, secondCard, orderOfCards, part):
    firstCard, secondCard = firstCard[0], secondCard[0]
    firstOne = cardsDealtWeight(firstCard) if part else cardsDealt(firstCard)
    secondOne = cardsDealtWeight(secondCard) if part else cardsDealt(secondCard)

    if firstOne != secondOne:
        if firstOne < secondOne:
            return -1
        if firstOne > secondOne:
            return 1
        return 0
    
    else:
        for element in range(5):
            x, y = orderOfCards.index(firstCard[element]), orderOfCards.index(secondCard[element])

            if x < y:
                return -1
            if x > y:
                return 1
            
    return 0

def partOne(LINES):
    LINES.sort(key=cmp_to_key(lambda x, y: compare(x, y, cardValuesP1, 0)))
    part1 = 0

    for i in range(len(LINES)):
        part1 += ((i + 1) * LINES[i][1])

    return part1

def partTwo(LINES):
    LINES.sort(key=cmp_to_key(lambda x, y: compare(x, y, cardValuesP2, 1)))
    part2 = 0
    for i in range(len(LINES)):
        part2 += ((i + 1) * LINES[i][1])
    return part2



if __name__ == "__main__":
    print('Part One: ', partOne(LINES), 'Part Two: ', partTwo(LINES) )