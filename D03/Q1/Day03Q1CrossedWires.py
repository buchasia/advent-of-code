from Point import Point

# In this method we implement minimum distance for crossed wires        
def getWireCoordinates(wirePath):
    # Here we assume that the Central port ist located at Point(0, 0)
    pathCoordinates = []
    currentPoint = Point(0, 0, True)
    pathCoordinates.append(currentPoint)
    for path in wirePath:
        pathStep = int(path[1:])
        if path[0] == 'D':
            currentPoint = currentPoint.moveDown(pathStep)
        elif path[0] == 'U':
            currentPoint = currentPoint.moveUp(pathStep)
        elif path[0] == 'L':
            currentPoint = currentPoint.moveLeft(pathStep)
        elif path[0] == 'R':
            currentPoint = currentPoint.moveRight(pathStep)
        pathCoordinates.append(currentPoint)
    return pathCoordinates 

def minDistanceCrossedWires(inputPath):

    distances = []
    
    # Open file for reading the two input sequence
    with open(inputPath) as fileP:

        # Read the path definition for the first wire 
        firstWire = fileP.readline().strip().split(',')
        
        # Read the path definition for the second wire
        secondWire = fileP.readline().strip().split(',')
        
        # get the path end points as coordinates
        firstWireCoordinates = getWireCoordinates(firstWire)

        # get the path end points as coordinates
        secondWireCoordinates = getWireCoordinates(secondWire)

        firstStart = firstWireCoordinates[0]
        for i in range(1, len(firstWireCoordinates)):
            firstEnd = firstWireCoordinates[i]
            secondStart = secondWireCoordinates[0]
            for j in range(1 , len(secondWireCoordinates)):
                secondEnd = secondWireCoordinates[j]
                intersectResult = Point.doIntersect(firstStart, firstEnd, secondStart, secondEnd)
                if intersectResult[0]:
                    distances.append(intersectResult[1])
                secondStart = secondEnd
            firstStart = firstEnd
            
    distances.sort()
    if len(distances) == 0:
        raise Exception('NoIntersection', 'The two wires do not intersect')
    return distances[0]

print(minDistanceCrossedWires('InputDay03Q1.txt'))
