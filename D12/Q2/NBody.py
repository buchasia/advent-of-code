
class NBody:
    def __init__(self, filePath):
        self.filePath = filePath
        self.coordinates = {}
        self.velocities = {}
        self.keySet = set()
    
    def getInitialCoordinates(self):
        index = 1
        # Open file for reading the input
        with open(self.filePath) as fileP:
            # Read the complete sequence and remove unwanted characters
            initialSequence = fileP.readline().strip()
            # <x=-4, y=-14, z=8>
            
            while initialSequence:
                # The sequence as List of integers
                #firstSplit = ['<x', '-4, y', '-14, z', '8>']
                firstSplit = initialSequence.split('=');
            
                # ['-4', ' y']
                [xVal, x] = firstSplit[1].split(',')
                xVal = int(xVal)

                # ['-14', ' z']
                [yVal, y] = firstSplit[2].split(',')
                yVal = int(yVal)

                # ['8', '']
                [zVal, z] = firstSplit[3].split('>')
                zVal = int(zVal)

                self.coordinates[index] = {'x': xVal, 'y': yVal, 'z': zVal}
                self.velocities[index] = {'x': 0, 'y': 0, 'z': 0}
                
                initialSequence = fileP.readline().strip()
                index += 1
        
    def runIteration(self, Axis):
        self.addHistory(0, Axis)
        i = -1
        while True:
            i += 1
            for bodyI in self.coordinates:
                for bodyJ in self.coordinates:
                    if bodyI == bodyJ:
                        continue
                    if self.coordinates[bodyI][Axis] > self.coordinates[bodyJ][Axis]:
                        self.velocities[bodyI][Axis] -= 1
                    elif self.coordinates[bodyI][Axis] < self.coordinates[bodyJ][Axis]:
                        self.velocities[bodyI][Axis] += 1
            for bodyI in self.coordinates:
                self.coordinates[bodyI][Axis] += self.velocities[bodyI][Axis]
            result = self.addHistory(i + 1, Axis)
            if result != False:
                return result
                

    def addHistory(self, iteration, axis):
        if iteration == 0:
            self.keyValue = self.getKey(axis)
            return

        if self.keyValue == self.getKey(axis):
            print(iteration, axis)
            return iteration
        else:
            return False

    def getKey(self, axis):
        keyValue = ''
        for body in self.coordinates:
            keyValue += str(self.coordinates[body][axis]) + ' '
            keyValue += str(self.velocities[body][axis]) + ' '
        return keyValue        
