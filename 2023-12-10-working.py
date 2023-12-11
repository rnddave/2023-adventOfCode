
def getInput():
    weAreLookingFor = None
    lines = [line.strip() for line in open("2023-12-10-puzzle-input", "r")]

    # from the reddit answer
    createAborder = "." * (len(lines[0]) + 2)
    PipeTile = [createAborder]

    for line in lines:
        PipeTile.append("." + line + ".")

    PipeTile.append(createAborder)

    # this bit doesn't work, need to revisit
    for row, line in enumerate(PipeTile):

        if "S" in line:
            weAreLookingFor = (row, line.index("S"))
            break

    return PipeTile, weAreLookingFor


def theRedditFunction(pipes, weAreHere):
    directionToMove = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }

    directionChanges = {
        "N": {"|": "N", "7": "W", "F": "E"},
        "E": {"-": "E", "7": "S", "J": "N"},
        "S": {"|": "S", "L": "E", "J": "W"},
        "W": {"-": "W", "L": "N", "F": "S"}
    }

    howManyMoves = 1
    howBigIsTheArea = 0
    whereAreWe = weAreHere

    # we start here (Sue)
    for direction in directionChanges:
        currentY, currentX = whereAreWe
        dirY, dirX = directionToMove[direction]
        if pipes[currentY + dirY][currentX + dirX] in directionChanges[direction]:
            directionNow = direction

    while whereAreWe != weAreHere or howManyMoves == 1:
        currentY, currentX = whereAreWe
        dirY, dirX = directionToMove[directionNow]
        howBigIsTheArea += currentX * dirY
        theNewX = currentX + dirX
        theNewY = currentY + dirY

        if pipes[theNewY][theNewX] == "S" and howManyMoves > 1:
            break
        whereAreWe = (theNewY, theNewX)
        directionNow = directionChanges[directionNow][pipes[theNewY][theNewX]]
        howManyMoves += 1

    return (howManyMoves // 2), (howBigIsTheArea - (howManyMoves // 2) + 1)


if __name__ == "__main__":

    getPipeMap, getStartingPos = getInput()
    
    furthestPoint, tilesCovered = theRedditFunction(getPipeMap, getStartingPos)
    
    print(f"part_one: {furthestPoint}") # 6786
    print(f"part_two: {tilesCovered}") # 495