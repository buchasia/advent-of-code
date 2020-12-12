def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    curWayEast = 10
    curWayNorth = 1
    curShipEast = 0
    curShipNorth = 0
    
    for line in fileLines:
        line = line.strip('\n')
        magnitude = int(line[1:])
        if line[0] == 'F':
            curShipEast += curWayEast * magnitude
            curShipNorth += curWayNorth * magnitude
        elif line[0] == 'N':
            curWayNorth += magnitude
        elif line[0] == 'S':
            curWayNorth -= magnitude
        elif line[0] == 'E':
            curWayEast += magnitude
        elif line[0] == 'W':
            curWayEast -= magnitude
        else:
            direction = line[0]
            [curWayEast, curWayNorth] = getCurrentDirection(curWayEast, curWayNorth, direction, magnitude)
    return abs(curShipEast) + abs(curShipNorth)
            
def getCurrentDirection(curWayEast, curWayNorth, direction, degree):
    if direction == 'R':
        direction = 'L'
        degree = 360 - degree
    if degree == 90:
        newEast = -1 * curWayNorth
        newNorth = curWayEast
    elif degree == 180:
        newEast = -1 * curWayEast
        newNorth = -1 * curWayNorth
    elif degree == 270:
        newEast = curWayNorth
        newNorth = -1 * curWayEast
    else:
        newEast = curWayEast
        newNorth = curWayNorth

    return [newEast, newNorth]

print(solveQuestion('InputD12Q2.txt'))


