# we need to scan through the puzzle input and
# decide if the game would have been possible within the limits of the following: 

# The bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes 

# we then need to need to add the id numbers from the games that would meet the criteria

# initial thoughts are to readline(input) and run through a sequence of If statements
# we also need to track which games would be possible so that we can extract the game ID from those
# the sum of the ID's = the answer to part 1

print('----------------------------------')
print('------------ PART ONE ------------')
print('----------------------------------')

# open the source data
with open("2023-12-02-puzzle-input") as file:
    # initialise the variable for tracking game IDs
    sumOfTheGameIDs = 0


    for line in file:
        countGame = True
        game, cubes = line.split(":")
        _, game = game.split()

        for sample in cubes.split(";"):

            for cube in sample.split(","):

                count, color = cube.split()
                count = int(count)

                if "red" in color and count > 12:
                    countGame = False
                if "blue" in color and count > 14:
                    countGame = False
                if "green" in color and count > 13:
                    countGame = False

        if countGame:
            sumOfTheGameIDs += int(game)
        
print(sumOfTheGameIDs) #2593 = correct



print('----------------------------------')
print('------------ PART TWO ------------')
print('----------------------------------')


with open("2023-12-02-puzzle-input") as file:
    sumOfTheGameIDs = 0

    for line in file:

        countGameP2 = True
        game, cubes = line.split(":")
        _, game = game.split()
        redMax, greenMax, blueMax = 1, 1, 1

        for sample in cubes.split(";"):

            for cube in sample.split(","):

                count, color = cube.split()
                count = int(count)

                if "red" in color and count > redMax:
                    redMax = count
                if "blue" in color and count > blueMax:
                    blueMax = count
                if "green" in color and count > greenMax:
                    greenMax = count
        
        countGameP2 += (redMax * blueMax * greenMax)
        
print(countGameP2) # 406 - seems far too low. INDEED - TOO LOW