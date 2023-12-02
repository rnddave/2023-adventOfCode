# cleaned up my code, moved my earlier brute-force attempts into a new file also in Github
# We need some place to hold the number-text relationship for Part 2
textToNumberDict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    }

def textToNumber(day1Input):
    text2numArr = []
    for line in day1Input:
        # if we see a match with dict key, replace with dic value
        for dictKey, dictValue in textToNumberDict.items():
            line = line.replace(dictKey, dictValue)
        text2numArr.append(line)

    # pass the newly populated array back
    return text2numArr

def getRidOfStrings(partTwo):
    partTwoNumber = 0

    for eachLine in partTwo:
        for char in eachLine:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(eachLine):
            if char.isdigit():
                last_digit = int(char)
                break
        lineItemTotal = int(str(first_digit) + str(last_digit))
        partTwoNumber += lineItemTotal

    return partTwoNumber


day1Input = open('2023-12-01-puzzle-input', 'r')
partTwo = textToNumber(day1Input) 


print(getRidOfStrings(partTwo)) # 52840 = CORRECT

day1Input.close()