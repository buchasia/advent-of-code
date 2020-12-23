from Program1202 import Program1202
from Operation import Operation

import os
import json

class ASCII:

    def __init__(self, inputPath):
        self.grid = {}
        self.inputPath = inputPath

    def getBoard(self, startValue):
        program = Program1202(self.inputPath, startValue)
        #inputData = ['A,B,A,C,A,A,C,B,C,B\nL,12,L,8,R,12\nL,10,L,8,L,12,R,12\nR,12,L,8,L,10\n' ]
        inputData = [65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 65, 44, 67, 44, 66, 44, 67, 44, 66, 10, 76, 44, 49, 50, 44, 76, 44, 56, 44, 82, 44, 49, 50, 10, 76, 44, 49, 48, 44, 76, 44, 56, 44, 76, 44, 49, 50, 44, 82, 44, 49, 50, 10, 82, 44, 49, 50, 44, 76, 44, 56, 44, 76, 44, 49, 48, 10, 110, 10]
        counter = 0
        while not program.isFinished():
            program.run(inputData[counter])
            counter += 1
            currentOutput = Operation.getOutput()            
            Operation.initializeOutput()
            self.getCameraView(currentOutput)
            #self.printCameraView()

        
        print(currentOutput)

        #self.getCameraView(currentOutput)

        #self.printCameraView()

        #print(self.getAlignmentParameter())

        #completePath = self.getCompletePath()

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

    def getCompletePath(self):
        completePath = self.getNextDirection()[1]
        isMoreDirection = True
        while isMoreDirection:
            completePath += str(self.getDirectionLength())
            #completePath += ',' + str(self.getDirectionLength())
            
            [isMoreDirection, nextDirection] = self.getNextDirection()
            if isMoreDirection:
                #completePath += ',' + nextDirection
                completePath += nextDirection
        print(completePath)
        return completePath
            
    def getDirectionLength(self):
        if self.robotDirection == 'L':
            return self.getLength(-1, 0)
        elif self.robotDirection == 'R':
            return self.getLength(1, 0)
        if self.robotDirection == 'D':
            return self.getLength(0, 1)
        elif self.robotDirection == 'U':
            return self.getLength(0, -1)

    def getLength(self, xMove, yMove):
        counter = 0
        while (self.robotBaseX + xMove >= 0 and self.robotBaseY + yMove >= 0 and
               self.robotBaseX + xMove < self.xDim and self.robotBaseY + yMove < self.yDim and
               self.grid[self.robotBaseY + yMove][self.robotBaseX + xMove] == '#'):
            self.robotBaseY += yMove
            self.robotBaseX += xMove
            counter += 1
        return counter
        
    def getNextDirection(self):
        if self.robotBaseX - 1 >= 0 and self.grid[self.robotBaseY][self.robotBaseX - 1] == '#' and self.robotDirection != 'R' and self.robotDirection != 'L':
            result = [True, self.moveLeft()]
            self.robotDirection = 'L'
            return result
        elif self.robotBaseX + 1 < self.xDim and self.grid[self.robotBaseY][self.robotBaseX + 1] == '#' and self.robotDirection != 'L' and self.robotDirection != 'R':
            result = [True, self.moveRight()]
            self.robotDirection = 'R'
            return result
        elif self.robotBaseY + 1 < self.yDim and self.grid[self.robotBaseY + 1][self.robotBaseX] == '#' and self.robotDirection != 'U' and self.robotDirection != 'D':
            result = [True, self.moveDown()]
            self.robotDirection = 'D'
            return result
        elif self.robotBaseY - 1 >= 0 and self.grid[self.robotBaseY - 1][self.robotBaseX] == '#' and self.robotDirection != 'D' and self.robotDirection != 'U':
            result = [True, self.moveUp()]
            self.robotDirection = 'U'
            return result
        return [False, '']

    def moveLeft(self):
        if self.robotDirection == 'U':
            return 'L'
        elif self.robotDirection == 'D':
            return 'R'

    def moveRight(self):
        if self.robotDirection == 'U':
            return 'R'
        elif self.robotDirection == 'D':
            return 'L'

    def moveUp(self):
        if self.robotDirection == 'L':
            return 'R'
        elif self.robotDirection == 'R':
            return 'L'      

    def moveDown(self):
        if self.robotDirection == 'L':
            return 'L'
        elif self.robotDirection == 'R':
            return 'R'
    
    def getCameraView(self, outputs):
        lineCount = 0
        counter = 0
        self.grid[lineCount] = []
        for output in outputs:
            counter += 1
            if output == 35:
                self.grid[lineCount].append('#')
            elif output == 10:
                lineCount += 1
                counter = 0
                self.grid[lineCount] = []
            elif output == 46:
                self.grid[lineCount].append('.')
            elif output == 60:
                self.robotBaseX = counter - 1
                self.robotBaseY = lineCount
                self.robotDirection = 'L'
                self.grid[lineCount].append('<')
            elif output == 62:
                self.robotBaseX = counter - 1
                self.robotBaseY = lineCount
                self.grid[lineCount].append('>')
                self.robotDirection = 'R'
            elif output == 94:
                self.robotBaseX = counter - 1
                self.robotBaseY = lineCount
                self.grid[lineCount].append('^')
                self.robotDirection = 'U'
            elif output == 118:
                self.robotBaseX = counter - 1
                self.robotBaseY = lineCount
                self.grid[lineCount].append('v')
                self.robotDirection = 'D'
                
                

inputPath = 'InputDay17.txt'

robot = ASCII(inputPath)

robot.getBoard(2)

#robot.getCompletePath()
