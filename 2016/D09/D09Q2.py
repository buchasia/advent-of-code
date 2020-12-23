def findLength(file):
    counter = -1
    bracketOpen = False
    repeatLength = ''
    repeatTimes = ''
    repeatLengthFound = False
    repeatTimesFound = False
    decomp = ''
    length = 0
    while counter < len(file) - 1:
        counter += 1
        if file[counter] == '(':
            bracketOpen = True
            continue
        if bracketOpen == False:
            length += 1
            continue
        elif file[counter] == 'x' and bracketOpen == True:
            repeatLength = int(repeatLength)
            repeatLengthFound = True
            continue
        elif file[counter] == ')' and bracketOpen == True:
            repeatTimes = int(repeatTimes)
            repeatTimesFound = True

        if bracketOpen != True:
            decomp += file[counter]
        else:
            if repeatLengthFound == True and repeatTimesFound == True:
                bracketOpen = False
                repeatString = file[(counter + 1):(counter + repeatLength + 1)]

                length += repeatTimes * findLength(repeatString)
                
                counter += repeatLength
                repeatLength = ''
                repeatTimes = ''
                repeatLengthFound = False
                repeatTimesFound = False

            else:
                if repeatLengthFound == False:
                    repeatLength += file[counter]
                else:
                    repeatTimes += file[counter]
    
    return length

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    file = fileLines[0]
    file = file.strip('\n')

    return findLength(file)

print(solveQuestion('InputD09Q2.txt'))
