# what the actual fudge - I have no idea how to even start this one!!! 

# read the input
# scan multi-line - multi-direction at same time ( ???????? )
# record the scores 
# (this bit seems inceonsequential at the moment, I can't even begin to think about how
# I would read a fdile in different directions)

#FILE = r"2023-12-03-puzzle-input"
#import sys

with open("2023-12-03-puzzle-input", 'r')  as file:
    
    lines = [f.rstrip() for f in file.readlines()]
    MissingPart = 0

    for linenum, line in enumerate(lines):
        idx = 0

        while idx < len(line):

            print('[1] did I get here?', line) # seem to be going in a loop for line 1 of the input

            # finding the numbers
            if line[idx].isdigit():

                print('[2] did I get here?') # I did NOT get here

                holder = 0
                startindex = idx
                endindex = idx

                while idx < len(line) and line[idx].isdigit():
                    endindex = idx
                    holder = holder * 10 + int(line[idx])
                    idx += 1

                # find the symbol
                symbolHere = False

                # symbol above
                if linenum - 1 >= 0:
                    i = startindex - 1

                    while i <= endindex + 1 and not symbolHere:

                        if i >=0 and i < len(line):
                            check = lines[linenum - 1][i]

                            if not check.isdigit() and check != ".":
                                symbolHere = True

                        i += 1

                # symbol is below
                if not symbolHere and linenum + 1 < len(lines):
                    i = startindex - 1

                    while i <= endindex + 1 and not symbolHere:

                        if i >=0 and i < len(line):
                            check = lines[linenum + 1][i]

                            if not check.isdigit() and check != ".":
                                symbolHere = True

                        i += 1

                # symbol is in same line
                if not symbolHere:
                    i = startindex - 1

                    if i >=0 and not line[i].isdigit() and line[i] != ".":
                        symbolHere = True

                i = endindex + 1

                if i < len(line) and not line[i].isdigit() and line[i] != ".":
                    symbolHere = True

                    if symbolHere:
                        MissingPart += holder
                idx += 1
            else:
                idx += 1

    print("Sum of part numbers = " + str(MissingPart)) # 45676 = WRONG  = too low - VERY TOO LOW