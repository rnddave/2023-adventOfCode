
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
                first_digit = int(char)
                break
        for char in reversed(eachLine):
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



