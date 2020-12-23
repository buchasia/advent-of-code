def solveProblem(inputPath):

    houseCoordinates = []
    with open(inputPath) as fileP:

        valueLine = str(fileP.readline()).strip('\n')

        currentHouseSantaX = 0
        currentHouseSantaY = 0
        currentHouseRoboX = 0
        currentHouseRoboY = 0
        
        houseCoordinates.append((0, 0))
        currentDirectionIndex = 0
        
        for direction in valueLine:
            if currentDirectionIndex % 2 == 0:
                [currentHouseSantaX, currentHouseSantaY] = nextCoordinate(direction, currentHouseSantaX, currentHouseSantaY)
                [currentHouseX, currentHouseY] = [currentHouseSantaX, currentHouseSantaY]
            else:
                [currentHouseRoboX, currentHouseRoboY] = nextCoordinate(direction, currentHouseRoboX, currentHouseRoboY)
                [currentHouseX, currentHouseY] = [currentHouseRoboX, currentHouseRoboY]

            currentDirectionIndex += 1
            
            if (currentHouseX, currentHouseY) in houseCoordinates:
                continue

            houseCoordinates.append((currentHouseX, currentHouseY))
                        
    return len(houseCoordinates)

def nextCoordinate(direction, currentHouseX, currentHouseY):
    if direction == '<':
        currentHouseX -= 1
    elif direction == '>':
        currentHouseX += 1
    elif direction == '^':
        currentHouseY -= 1
    elif direction == 'v':
        currentHouseY += 1

    return [currentHouseX, currentHouseY]


print(solveProblem('InputD03Q1.txt'))
