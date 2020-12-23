import numpy

class FFT:

    def __init__(self, inputPath, pattern, numberPhase):
        self.numberPhase = numberPhase
        self.inputPath = inputPath
        self.pattern = pattern

    def printFirst8(self, phaseNumber):
        
        print(phaseNumber, ''.join([str(digit) for digit in self.phaseData[:8]]))
    
    def getPattern(self):
        self.getInitialPattern()

        #print("initial", self.phaseData)

        self.getPatternMatrix()

        for i in range(0, self.numberPhase):
            self.phaseDataMatrix = numpy.matmul(self.patternMatrix, numpy.array(self.phaseData).reshape(len(self.phaseData), 1))
            counter = 0
            for element in self.phaseDataMatrix:
                self.phaseData[counter] = abs(element.item(0)) % 10
                counter += 1
        self.printFirst8(self.numberPhase)

    def getInitialPattern(self):
        # Open file for reading the input sequence
        with open(self.inputPath) as fileP:
            # Read the complete sequence and remove unwanted characters
            initialSequence = fileP.read().strip()

            # The sequence as List of integers
            self.phaseData = [int(digit) for digit in initialSequence];
        
    
    def getPatternMatrix(self):
        patternRows = []
        maxLength = len(self.phaseData)
        for j in range(1, maxLength + 1):
            patternMulti = []
            while len(patternMulti) < maxLength + 1:
                for patternDigit in self.pattern:
                    for i in range(0, j):
                        patternMulti.append(patternDigit)
                        if len(patternMulti) >= maxLength + 1:
                            break
                    if len(patternMulti) >= maxLength + 1:
                        break
                if len(patternMulti) >= maxLength + 1:
                    break
            patternRows.append(patternMulti[1:(maxLength + 1)])
            
        self.patternMatrix = numpy.matrix(patternRows)

inputPath = 'InputDay16.txt'

# Question 1
robot = FFT(inputPath, [0, 1, 0, -1], 100)

robot.getPattern()
