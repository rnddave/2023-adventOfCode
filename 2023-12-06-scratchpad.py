def onTheSixthDayOfChristmas(time, distance):
    theAnswer = [hold for hold in range(2, time-1) if (time - hold) * hold > distance]
    
    # Return the results
    return theAnswer

with open("2023-12-06-puzzle-input", "r") as file:
    lineData = file.read().split("\n")

    _, time = lineData[0].split(": ")
    _, distance = lineData[1].split(": ")

    time = list(map(int, time.split()))
    distance = list(map(int, distance.split()))

# sixGeesALaying
sixGeese_A_Laying = []

for eachItem in range(len(time)):
    theAnswer = onTheSixthDayOfChristmas(time[eachItem], distance[eachItem])
    sixGeese_A_Laying.append(len(theAnswer))

theAnswer = 1


for theNumber in sixGeese_A_Laying:
    theAnswer *= theNumber

# Day 6 / part 1
print(theAnswer) # 781200 = correct