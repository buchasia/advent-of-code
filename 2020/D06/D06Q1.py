def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    totalCount = 0
    answeredQuestion = []
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")

        if valueLine == "":
            answeredQuestion = []
            continue
        
        for question in valueLine:
            if question in answeredQuestion:
                continue

            totalCount += 1

            answeredQuestion.append(question)

    return totalCount

print(solveQuestion('InputD06Q1.txt'))
