
# below is the example data:
a = '1abc2'
b = 'pqr3stu8vwx'
c = 'a1b2c3d4e5f'
d = 'treb7uchet'

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
# Adding these together produces 142.

# we could use isdigit to find all digits:
print(int(''.join(filter(str.isdigit, a)))) # 12

# but this will also find multiple digits in a string:

print(int(''.join(filter(str.isdigit, c)))) # 12345 (answer needs to be 15)


# could use above to get all digits and then run the output from that into a function to find the first/last ?? 

# Find the first digit
def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10: 
        n = n / 10
     
    # return the first digit
    return int(n)
 
# Find the last digit
def lastDigit(n) :
 
    # return the last digit
    return (n % 10)
 
# Driver Code
n = 98562
print(firstDigit(n), end = "") 
print(lastDigit(n))
# 92


#############
# 1. take input from the file
# 2. get the digits from the strings
# 3. then get the 1st and last digit from the output of 2
# 4. if a string has a single digit, we need to handle that with a duplication of the single digit

##############
# 1. get the input 

file1 = open('2023-12-01-puzzle-input', 'r')
 
while True:
    # Get next line from file
    line = file1.readline()
    # if line is empty end of the file is reached
    if not line:
        break

    print(line.strip())
 
file1.close()

# 2. get the digits from the strings

file1 = open('2023-12-01-puzzle-input', 'r')
 
while True:
    # Get next line from file
    line = file1.readline()
    # if line is empty end of the file is reached
    if not line:
        break

    # get the digits from the strings
    print(int(''.join(filter(str.isdigit, line))))
 
file1.close()

# 3. then get the 1st and last digit from the output of 2

print('----------------------------------')

day1Input = open('2023-12-01-puzzle-input', 'r')
eachLine = day1Input.readline()


def withoutFuncFirstLineSkips(input):
    partOneNumber = 0

    for eachLine in day1Input:
        for char in eachLine:
            if char.isdigit():
                first_digit = int(char) # gets the first digit (left to right)
                break
        for char in reversed(eachLine): # gets frist digit (right to left) = this solfves the single digit problem
            if char.isdigit():
                last_digit = int(char)
                break
        lineItemTotal = int(str(first_digit) + str(last_digit))
        partOneNumber += lineItemTotal

    return partOneNumber

print(withoutFuncFirstLineSkips(eachLine)) # 53957 = WRONG (too Low) but seems to be because missing first line
day1Input.close()


print('----------------------------------')

def withoutFuncFirstLineSkips(input):
    partOneNumber = 0

    for eachLine in day1Input:
        for char in eachLine:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(eachLine):
            if char.isdigit():
                last_digit = int(char)
                break
        lineItemTotal = int(str(first_digit) + str(last_digit))
        partOneNumber += lineItemTotal

    return partOneNumber

day1Input = open('2023-12-01-puzzle-input', 'r')
# I will just pass the whole file into the function
print("Part 1:",  withoutFuncFirstLineSkips(day1Input)) # Part 1: 53974 = correct
day1Input.close()

print('----------------------------------')
print('------------ PART TWO ------------')
print('----------------------------------')

# wtf! 
# not sure I get this one tbh... 

# okay so we need some place to hold the number-text relationship I think 
textToNumberDict = {
    "one": "1", 
    "two": "2", 
    "three": "3",
    "four": "4", 
    "five": "5", 
    "six": "6",
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
    }

# we need to convert the text to numbers, 
# I think from what we tried for part one, a function will work best
def textToNumber(day1Input):
    text2numArr = []
    for line in day1Input:
        # if we see a match with dict key, replace with dic value
        for dictKey, dictValue in textToNumberDict.items():
            line = line.replace(dictKey, dictValue)
        text2numArr.append(line)

    # pass the newly populated array back
    return text2numArr

# lets open the source file again
day1Input = open('2023-12-01-puzzle-input', 'r')

# new var to record output from textToNumber function
dayOnePartTwo = textToNumber(day1Input)

# I am getting 0 for some reason (part 2) but when I run this line I can see that the array is populated)
# print(dayOnePartTwo)

# ORDER of FUNCTIONS!!

# we now want to pass the output from textToNumber() to our part 1 function = withoutFuncFirstLineSkips()
withoutFuncFirstLineSkips(dayOnePartTwo)
print("Part 2:",  withoutFuncFirstLineSkips(dayOnePartTwo)) # 0 {??? wtf did I do this time}
day1Input.close()

###### AHH, I am passing an array now, not a file containing new-lines, need to rething part 1 function ######

# We need some place to hold the number-text relationship for Part 2
textToNumberDict = {
    "one": "1", 
    "two": "2", 
    "three": "3",
    "four": "4", 
    "five": "5", 
    "six": "6",
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
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


print(getRidOfStrings(partTwo)) #  52155 - WRONG (TOO LOW)

day1Input.close()



print('----------------------------------------------------------------')
print('----------- ABOVE WAS ME BRUTE-FORCING MY WAY THOURH -----------')
print('----------------------------------------------------------------')
print('----------------------------------------------------------------')
print('------------------- BELOW IS MY FINAL ANSWER -------------------')
print('----------------------------------------------------------------')

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

# ARRRRGGGHHH - THIS IS DAY ONE - SO DAMN HARD 
# - the overlapping text like Twone (in which case two was replaced by 2 and then One was just 'ne' 
# therefore not caught was really fudging hard to find an answer to - HOURS on this 
# before I looked at subreddit for a tip and saw someone else had used the str2num to with 
# clever'er replacements than I)

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