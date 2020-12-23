import numpy

class FFT:

    def __init__(self, inputPath, pattern, numberPhase, repeat):
        self.numberPhase = numberPhase
        self.inputPath = inputPath
        self.pattern = pattern
        self.repeat = repeat

    def printFirst8(self, phaseNumber):
        
        print(phaseNumber, ''.join([str(digit) for digit in self.phaseData[:8]]))
    
    def getPattern(self):
        self.getInitialPattern()

        #print("initial", self.phaseData)

        for _ in range(0, self.numberPhase):
            digit = 0
            for i in range(len(self.phaseData) - 1 , -1, -1):
                digit = (self.phaseData[i] + digit) % 10
                self.phaseData[i] = digit
        self.printFirst8(self.numberPhase)

    def getInitialPattern(self):
        # Open file for reading the input sequence
        with open(self.inputPath) as fileP:
            # Read the complete sequence and remove unwanted characters
            initialSequence = fileP.read().strip()

            # The sequence as List of integers
            tempData = [int(digit) for digit in initialSequence];

            self.phaseData = []
            for i in range(0, self.repeat):
                self.phaseData.extend(tempData)

            self.offset = int(''.join([str(digit) for digit in self.phaseData[0:7]]))
            self.phaseData = self.phaseData[self.offset:]
            print(len(self.phaseData))
            
inputPath = 'InputDay16.txt'

# Question 1
robot = FFT(inputPath, [0, 1, 0, -1], 100, 10000)

robot.getPattern()
