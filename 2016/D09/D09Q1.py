def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    file = fileLines[0]
    file = file.strip('\n')

    fileLength = len(file)

    counter = -1
    bracketOpen = False
    repeatLength = ''
    repeatTimes = ''
    repeatLengthFound = False
    repeatTimesFound = False
    decomp = ''
    
    while counter < fileLength - 1:
        counter += 1
        if file[counter] == '(':
            bracketOpen = True
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
                for i in range(repeatTimes):
                    decomp += repeatString
                    
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
    
    return len(decomp)

print(solveQuestion('InputD09Q1.txt'))
