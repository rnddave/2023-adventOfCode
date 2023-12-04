# read a line
# split at the | (pipe)
# compare LEFT | RIGHT 
# count number of matches (per line) doubling as we go
# count total number of matches (sum of all the winning lines)


# Function to convert a list of strings to a list of integers
def convert_to_int(array):
    return list(map(int, array))

# Open the file for reading
with open("2023-12-04-puzzle-input", "r") as file:

    # I forgot about the card x: - need to discard this bit
    lineInput = [line.strip().split(": ")[1] for line in file.readlines()]
    
    # two parts (split at the pipe)
    lineInput = [(numbers[0].split(), numbers[1].split()) 
             for numbers in [line.split(" | ") for line in lineInput]]

# Initialise Part 1 variables 
# lineInputPoints = 0 # ( this needs to be in the FOR loop )
totalPoints = 0

# Initialise Part 2 variables 
numberOfCardsForMe = 1 # reddit said I should initialise to 0 but not sure why
cardInitialValue = [1] * len(lineInput)


# Loop through each pair of [winning numbers] and [my numbers]
for (aSideNumbers, bSideNumbers) in lineInput:
    lineInputPoints = 0
    # Reddit suggest function to do this bit because mine does not work
    # aSideNumbers = list(map(int(winning_numbers))) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
    aSideNumbers = convert_to_int(aSideNumbers) 

    # Compare [my numbers] with [winning numbers] to calculate points
    for myNumbers in convert_to_int(bSideNumbers):
        if myNumbers in aSideNumbers:
            lineInputPoints += 1

    # Update the [total points] based on the [calculated points]
    totalPoints += 2 ** (lineInputPoints-1) if lineInputPoints > 0 else 0


    # PART 2 - NEW SCRATCH CARDS
    # Update the number of scratchcards based on points
    howMany = numberOfCardsForMe

    for card in range(lineInputPoints):
        cardInitialValue[howMany+card] += 1 * cardInitialValue[numberOfCardsForMe-1]

    # Update the number of [winning cards]
    numberOfCardsForMe += 1 
    # part2 = sum(range(numberOfCardsForMe))

# output PART 1 attempt 1
# print(f"Output Part One {totalPoints}") # 27541513926103116840762798990565337283274206650153010829433225163847466280910629336816668583077582891504992220256602857508206504525461214505452075123715269136811634286446707081247266105496960846738476439335937837978128974391618068303142449192777205034177200525177179960879937658883376884613632

# output PART 1 attempt 2
print("Part One = ", totalPoints ) # Part One =  25231 = CORRECT

# output PART 2 attempt 1
# print("Part Two = ", numberOfCardsForMe) # 212 = WRONG too low

# output PART 2 attempt 2
# print("Part Two = ", numberOfCardsForMe) # 213 = WRONG too low (this is just because I changed the index starting count to 1 per reddit)

# output PART 2 attempt 3 ( reddit advised I should be summing up the output of my winning cards)
# print(part2) # 22578 = WRONG = TOO LOW

# output PART 2 attempt 4 
print(f"Part 2 = {sum(numberOfCardsForMe)}")

