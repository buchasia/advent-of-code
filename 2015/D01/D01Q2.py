def solveProblem(inputPath):

    floor = 0
    indexFloorInfo = 0
    
    with open(inputPath) as fileP:

        valueLine = fileP.readline()
        
        for floorInfo in valueLine:
            indexFloorInfo += 1
            if floorInfo == '(':
                floor += 1
            elif floorInfo == ')':
                floor -= 1
            if floor == -1:
                return indexFloorInfo
                

print(solveProblem('InputD01Q2.txt'))
