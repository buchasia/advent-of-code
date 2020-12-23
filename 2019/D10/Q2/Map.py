class AsteroidMap:
    def __init__(self, filePath):
        self.filePath = filePath
        self.maxX = 0
        self.maxY = 0
        self.traversed = []
        self.initialTraversed = []
        self.mapData = []
        self.asteroidCoord = []
        self.getMapData()

    def getDistanceSlopeMap(self):
        slopeDistance = {}

        self.getMonitoringStationLocation()

        stationX = self.monitoringStation[0][0]
        stationY = self.monitoringStation[0][1]

        print(stationX, stationY)

        for aCoord in self.asteroidCoord:
            distance = (stationX - aCoord[0])*(stationX - aCoord[0]) + (stationY - aCoord[1])*(stationY - aCoord[1])
            if stationX == aCoord[0]:
                slope = self.maxY
            else:
                slope = -(stationY - aCoord[1])/(stationX - aCoord[0])
            # Compute Quadrant
            diffX = aCoord[0] - stationX
            diffY = aCoord[1] - stationY

            if diffX > 0 and diffY > 0:
                quadrant = 2
            elif diffX >= 0 and diffY <= 0:
                quadrant = 1
            elif diffX < 0 and diffY < 0:
                quadrant = 4
            else:
                quadrant = 3

            if slope in slopeDistance:
                if distance in slopeDistance[slope]:
                    slopeDistance[slope][distance][quadrant] =  [aCoord[0], aCoord[1]]
                else:
                    slopeDistance[slope][distance] = {}
                    slopeDistance[slope][distance][quadrant] = [aCoord[0], aCoord[1]]
            else:
                slopeDistance[slope] = {}
                slopeDistance[slope][distance] = {}
                slopeDistance[slope][distance][quadrant] = [aCoord[0], aCoord[1]]

        counter = 1
        tempCounter = 0
        currentQuadrant = 0
        while True:
            currentQuadrant += 1
            if currentQuadrant == 5:
                currentQuadrant = 1
            if currentQuadrant == 1:
                if tempCounter == counter:
                    break
                tempCounter = counter
            
            for slopeKey in sorted(slopeDistance.keys(), reverse=True):
                distanceDict = slopeDistance[slopeKey]
                for distKey in sorted(distanceDict.keys()):
                    if distKey == 0:
                        distanceDict.pop(distKey)
                        continue
                    quadrantDict = distanceDict[distKey]
                    if currentQuadrant in quadrantDict:
                        if counter == 200:
                            print(counter, slopeKey, currentQuadrant, distKey, quadrantDict[currentQuadrant])
                        counter += 1
                        quadrantDict.pop(currentQuadrant)
                        break

            
    
    def getMonitoringStationLocation(self):
        possibleXDiff = list(range(0, self.getMaxX()))
        possibleYDiff = list(range(0, self.getMaxY()))

        possibleReach = {}
    
        for asteroid in self.getAsteroidCoordinates():
            count = 0
            self.createNewTraversed()
            for xDiff in possibleXDiff:
                for yDiff in possibleYDiff:
                    if xDiff == 0 and yDiff == 0:
                        continue
                    count += self.findAsteroidsInPath(asteroid[0], asteroid[1], xDiff, yDiff)
                    if self.traversedAll():
                        break
                if self.traversedAll():
                    break
    
            possibleReach[(asteroid[0], asteroid[1])] = count

        possibleReach = sorted(possibleReach.items(), key = lambda item: item[1], reverse = True)
        self.monitoringStation = possibleReach[0]

        return possibleReach[0]
    
    def getMapData(self):
        # Open file for reading the input sequence
        with open(self.filePath) as fileP:
            # Read the complete sequence and remove unwanted characters
            mapLine = fileP.readline().strip()
    		
            y = 0
	    
            while mapLine:
                self.mapData.append([])
                self.initialTraversed.append([])
                # The sequence as List of integers
                x = 0
                for mapValue in mapLine:
                    self.mapData[y].append(mapValue)
                    self.initialTraversed[y].append(False)
                    if mapValue == '#':
                        self.asteroidCoord.append([x, y])
                    x += 1
                    
                y += 1
                mapLine = fileP.readline().strip()
        self.maxX = len(self.mapData[0])
        self.maxY = len(self.mapData)
        
    def getAsteroidCoordinates(self):
        return self.asteroidCoord

    def getMaxX(self):
        return self.maxX

    def getMaxY(self):
        return self.maxY


    def findAsteroidsInPath(self, xStart, yStart, xDiff, yDiff):
        countFound = 0
        
        if self.isAsteroidInPath(xStart, yStart, xDiff, yDiff):
            countFound += 1

        if self.isAsteroidInPath(xStart, yStart, -xDiff, -yDiff):
            countFound += 1

        if self.isAsteroidInPath(xStart, yStart, xDiff, -yDiff):
            countFound += 1

        if self.isAsteroidInPath(xStart, yStart, -xDiff, yDiff):
            countFound += 1

        self.traversed[yStart][xStart] = True

        return countFound

    def createNewTraversed(self):
        self.traversed = []
        for row in self.initialTraversed:
            self.traversed.append(list(row))

    def traversedAll(self):
        for row in self.traversed:
            for element in row:
                if not element:
                    return False
        return True
    
    def isAsteroidInPath(self, xStart, yStart, xDiff, yDiff):
        currentX = xStart + xDiff
        currentY = yStart + yDiff
        isFound = False
        while (currentX >= 0 and currentX < self.maxX and currentY >= 0 and currentY < self.maxY):
            if not self.traversed[currentY][currentX]:
                self.traversed[currentY][currentX] = True
                if self.mapData[currentY][currentX] == '#':
                    isFound = True

            currentX += xDiff
            currentY += yDiff
        return isFound
