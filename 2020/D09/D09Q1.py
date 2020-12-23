def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    currentBuffer = []
    for valueLine in fileLines:
        valueLine = int(valueLine)
        if len(currentBuffer) < 25:
            currentBuffer.append(valueLine)
        else:
            found = False
            for number in currentBuffer:
                if (valueLine - number) in currentBuffer and valueLine - number != number:
                    found = True
                    break

            if found == True:
                currentBuffer.append(valueLine)        
                currentBuffer.pop(0)
            else:
                return valueLine
                
            
        
print(solveQuestion('InputD09Q1.txt'))
