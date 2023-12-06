def onTheSixthDayOfChristmas(time, distance):
    theAnswer = [hold for hold in range(2, time - 1) if (time - hold) * hold > distance]
    
    # Return the results
    return theAnswer

def onTheSixthDayOfChristmasPartTwo(timeP2, distanceP2):
    theAnswerP2 = [hold for hold in range(2, timeP2 - 1) if (timeP2 - hold) * hold > distanceP2]
    
    # Return the results
    return len(theAnswerP2)


with open("2023-12-06-puzzle-input", "r") as file:
    lineData = file.read().split("\n")

    _, time = lineData[0].split(": ")
    _, distance = lineData[1].split(": ")

    time = list(map(int, time.split()))
    distance = list(map(int, distance.split()))

    _, timeP2 = lineData[0].split(": ")
    _, distanceP2 = lineData[1].split(": ")

    timeP2 = int("".join(timeP2.split()))
    distanceP2 = int("".join(distanceP2.split()))

# sixGeesALaying
sixGeese_A_Laying = []

for eachItem in range(len(time)):
    theAnswer = onTheSixthDayOfChristmas(time[eachItem], distance[eachItem])
    sixGeese_A_Laying.append(len(theAnswer))

theAnswer = 1

for theNumber in sixGeese_A_Laying:
    theAnswer *= theNumber

# Day 6 / part 1
# print("Part One: ", theAnswer) # 781200 = correct

theAnswerP2 = onTheSixthDayOfChristmasPartTwo(timeP2, distanceP2)

# Day 6 / Part 2
# print("Part Two: ", theAnswerP2) # 49240091 = correct
# interestingly, there was a delay when running Part Two and I thought I'd created an infinite loop, guess I should re-run with the timer in place: 

