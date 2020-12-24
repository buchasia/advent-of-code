import timeit

# This function returns the input data in the form that can later be used directly
def getInputData(inputPath):
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    return [line.strip() for line in fileLines]

# Move Offsets for different directions, this helps in identfying where to move faster
moveOffset = {'ne': (1, 1), 'nw': (-1, 1), 'sw': (-1, -1), 'se': (1, -1), 'e': (2, 0), 'w': (-2, 0)}

# Color Switch made easy ;)
colorSwitch = {'B': 'W', 'W': 'B'}

# This function returns the initial configuration for day 0 (Part 1)
def initialConfig(inputData):
    identified ={}

    # For each line in the input data we need to identify the location of the hexagoen from
    # a reference that needs to be flipped. All hexagons start with 'White' face up
    for line in inputData:
        counter = -1
        currentX = 0
        currentY = 0
        while counter < len(line) - 1:
            counter += 1

            # If the next character in the instruction starts with an 's' or an 'n' we need to
            # also take the next chracter to get the complete direction 'se', 'sw', 'ne' or 'nw'
            if line[counter] == 's' or line[counter] == 'n':
                nextDirection = line[counter:counter + 2]
                counter += 1
            else:
                nextDirection = line[counter]

            # Then we compute the new current location after this move
            currentX += moveOffset[nextDirection][0]
            currentY += moveOffset[nextDirection][1]

        # If the hexagon at the current location is not in our list, we set it to its default color up
        # and add to the list
        if (currentX, currentY) not in identified:
            identified[(currentX, currentY)] = 'W'

        # Identified hexagon is flipped
        identified[(currentX, currentY)] = colorSwitch[identified[(currentX, currentY)]]

    return identified

# This function simulates the next days after the initial configuration has been placed
def getNumberofBlackAfterDays(identified, days):

    # We do the simulation for a given number of days. 
    for i in range(days):
        newCoord = dict(identified)
        seen = set()

        # For each identified hexagon from previous day we identify all adjacent hexagons and
        # count number of black hexagons adjacent to them and apply the problem rules to get the
        # the next days hexagon configuration
        for coord in identified:
            moveOffset1 = dict(moveOffset)

            # We also want to consider the current hexagon, this we do by adding 'noMove' with offset
            # (0,0)
            moveOffset1['noMove'] = ((0, 0))
            for offset in moveOffset1:

                # The following gives the location of the hexagon that we want to consider next
                currentX = coord[0] + moveOffset1[offset][0]
                currentY = coord[1] + moveOffset1[offset][1]

                if (currentX, currentY) in seen:
                    continue
                else:
                    seen.add((currentX, currentY))

                blackCount = 0

                # This will identify all adjacent hexagons that we need to identify for the current
                # hexagon under consideration
                for offset1 in moveOffset:
                    currentXX = currentX + moveOffset[offset1][0]
                    currentYY = currentY + moveOffset[offset1][1]
                    
                    if (currentXX, currentYY) in identified:
                        if identified[(currentXX, currentYY)] == 'B':
                            blackCount += 1

                if (currentX, currentY) not in identified:
                    newCoord[(currentX, currentY)] = 'W'

                # Apply problem rules to get the new configuration for the current hexagon under consideration
                if (currentX, currentY) not in identified:
                    if blackCount == 2:
                        newCoord[(currentX, currentY)] = 'B'
                    else:
                        newCoord[(currentX, currentY)] = 'W'
                else:
                    if identified[(currentX, currentY)] == 'B' and (blackCount == 0 or blackCount > 2):
                        newCoord[(currentX, currentY)] = 'W'
                    elif identified[(currentX, currentY)] == 'W' and blackCount == 2:
                        newCoord[(currentX, currentY)] = 'B'
        identified = dict(newCoord)
    return identified
                

def solveParts(inputData, partOne = True, days=100):
    identified = initialConfig(inputData)
    if partOne:
        return sum([1 for coord in identified if identified[coord] == 'B'])
    else:
        identified = getNumberofBlackAfterDays(identified, days)
        return sum([1 for coord in identified if identified[coord] == 'B'])
    
def solve(inputPath):
    inputData = getInputData(inputPath)
    
    print([solveParts(inputData),
           solveParts(inputData, partOne = False, days=100)])

#Timer Start
start = timeit.default_timer()

solve('D24.txt')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
