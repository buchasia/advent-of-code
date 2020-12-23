
class NBody:
    def __init__(self, filePath, numIteration):
        self.filePath = filePath
        self.coordinates = {}
        self.velocities = {}
        self.numIteration = numIteration
    
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
        print(self.coordinates)
        print(self.velocities)

    def runIteration(self):
        self.printCurrentState(0)
        for i in range(0, self.numIteration):
            for bodyI in self.coordinates:
                for bodyJ in self.coordinates:
                    if bodyI == bodyJ:
                        continue
                    if self.coordinates[bodyI]['x'] > self.coordinates[bodyJ]['x']:
                        self.velocities[bodyI]['x'] -= 1
                    elif self.coordinates[bodyI]['x'] < self.coordinates[bodyJ]['x']:
                        self.velocities[bodyI]['x'] += 1
                    if self.coordinates[bodyI]['y'] > self.coordinates[bodyJ]['y']:
                        self.velocities[bodyI]['y'] -= 1
                    elif self.coordinates[bodyI]['y'] < self.coordinates[bodyJ]['y']:
                        self.velocities[bodyI]['y'] += 1
                    if self.coordinates[bodyI]['z'] > self.coordinates[bodyJ]['z']:
                        self.velocities[bodyI]['z'] -= 1
                    elif self.coordinates[bodyI]['z'] < self.coordinates[bodyJ]['z']:
                        self.velocities[bodyI]['z'] += 1
            for bodyI in self.coordinates:
                self.coordinates[bodyI]['x'] += self.velocities[bodyI]['x']
                self.coordinates[bodyI]['y'] += self.velocities[bodyI]['y']
                self.coordinates[bodyI]['z'] += self.velocities[bodyI]['z']
        self.printCurrentState(self.numIteration)

    def printCurrentState(self, iteration):
        total = 0
        for body in self.coordinates:
            potential = abs(self.coordinates[body]['x']) + abs(self.coordinates[body]['y']) + abs(self.coordinates[body]['z'])
            kinetic = abs(self.velocities[body]['x']) + abs(self.velocities[body]['y']) + abs(self.velocities[body]['z'])
            total += potential * kinetic
        print('Total Energy as Iteration', iteration, ' is = ', total)
        
