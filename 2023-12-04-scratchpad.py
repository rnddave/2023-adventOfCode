# read a line
# split at the | (pipe)
# compare LEFT | RIGHT 
# count number of matches (per line) doubling as we go
# count total number of matches (sum of all the winning lines)


# Function to convert a list of strings to a list of integers
def convert_to_int(array):
    return list(map(int, array))

# Initialise variables
lineInputPoints = 0
totalPoints = 0

# Open the file for reading
with open("2023-12-04-puzzle-input", "r") as file:

    # I forgot about the card x: - need to discard this bit
    lineInput = [line.strip().split(": ")[1] for line in file.readlines()]
    
    # two parts (split at the pipe)
    lineInput = [(numbers[0].split(), numbers[1].split()) 
             for numbers in [line.split(" | ") for line in lineInput]]

# Loop through each pair of winning_numbers and your_numbers
for (aSideNumbers, bSideNumbers) in lineInput:
    # Reddit suggest function to do this bit because mine does not work
    # aSideNumbers = list(map(int(winning_numbers))) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
    aSideNumbers = convert_to_int(aSideNumbers) 

    # Compare your numbers with winning numbers to calculate points
    for myNumbers in convert_to_int(bSideNumbers):
        if myNumbers in aSideNumbers:
            lineInputPoints += 1

        # Update the total points based on the calculated points
    totalPoints += 2 ** (lineInputPoints-1) if lineInputPoints > 0 else 0

# Print the total points
print(f"Output Part One {totalPoints}") # 27541513926103116840762798990565337283274206650153010829433225163847466280910629336816668583077582891504992220256602857508206504525461214505452075123715269136811634286446707081247266105496960846738476439335937837978128974391618068303142449192777205034177200525177179960879937658883376884613632