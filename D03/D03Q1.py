def solveProblem(inputPath):

    houseCoordinates = []
    with open(inputPath) as fileP:

        valueLine = str(fileP.readline()).strip('\n')

        currentHouseX = 0
        currentHouseY = 0

        houseCoordinates.append((0, 0))
        
        for direction in valueLine:
            if direction == '<':
                currentHouseX -= 1
            elif direction == '>':
                currentHouseX += 1
            elif direction == '^':
                currentHouseY -= 1
            elif direction == 'v':
                currentHouseY += 1

            if (currentHouseX, currentHouseY) in houseCoordinates:
                continue

            houseCoordinates.append((currentHouseX, currentHouseY))
                        
    return len(houseCoordinates)

print(solveProblem('InputD03Q1.txt'))
