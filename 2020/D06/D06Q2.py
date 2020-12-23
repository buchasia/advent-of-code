def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    totalCount = 0
    answeredQuestion = {}
    currentGroupSize = 0
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")

        if valueLine == "":
            for question in answeredQuestion:
                if answeredQuestion[question] == currentGroupSize:
                    totalCount += 1

            answeredQuestion = {}
            currentGroupSize = 0
            continue

        currentGroupSize += 1
        
        for question in valueLine:
            if question in answeredQuestion:
                answeredQuestion[question] += 1
            else:
                answeredQuestion[question] = 1

    for question in answeredQuestion:
        if answeredQuestion[question] == currentGroupSize:
            totalCount += 1

    return totalCount

print(solveQuestion('InputD06Q2.txt'))
