from Program1202 import Program1202
from Operation import Operation

import os
import json

class ASCII:

    def __init__(self, inputPath):
        self.grid = {}
        self.inputPath = inputPath

    def getBoard(self, startValue):
        program = Program1202(self.inputPath)
        program.run(None)
        currentOutput = Operation.getOutput()
        Operation.initializeOutput()

        self.getCameraView(currentOutput)

        self.printCameraView()

        print(self.getAlignmentParameter())

    def getAlignmentParameter(self):
        self.yDim = len(self.grid) - 2
        self.xDim = len(self.grid[0])
        aligmentParameter = 0
        for y in range(1, self.yDim - 1 ):
            for x in range(1, self.xDim - 1):
                if (self.grid[y][x] == '#'):
                    if(self.grid[y - 1][x] == '#' and
                       self.grid[y + 1][x] == '#' and
                       self.grid[y][x - 1] == '#' and
                       self.grid[y][x + 1] == '#'):
                        aligmentParameter += y * x
        return aligmentParameter
    def printCameraView(self):
        self.yDim = len(self.grid) - 1

        board = ''
        for i in range(0, self.yDim):
            board += ''.join(self.grid[i]) + "\n"

        print(board)

    

    def getCameraView(self, outputs):
        lineCount = 0
        self.grid[lineCount] = []
        for output in outputs:
            if output == 35:
                self.grid[lineCount].append('#')
            elif output == 10:
                lineCount += 1
                self.grid[lineCount] = []
            elif output == 46:
                self.grid[lineCount].append('.')
            elif output == 60:
                self.grid[lineCount].append('<')
            elif output == 62:
                self.grid[lineCount].append('>')
            elif output == 94:
                self.grid[lineCount].append('^')
            elif output == 118:
                self.grid[lineCount].append('<')
                
                
                

inputPath = 'InputDay17.txt'

robot = ASCII(inputPath)

robot.getBoard(0)
