def solveProblem(inputPath):

    floor = 0
    
    with open(inputPath) as fileP:

        valueLine = fileP.readline()

        for floorInfo in valueLine:
            if floorInfo == '(':
                floor += 1
            elif floorInfo == ')':
                floor -= 1
                
    return floor

print(solveProblem('InputD01Q1.txt'))
