from Program1202 import Program1202
from Operation import Operation

import os
import json

class OxygenSystem:

    def __init__(self, inputPath):
        self.grid = {}
        self.currentX = 25
        self.currentY = 22
        self.grid[str(self.currentX) + " " + str(self.currentY)] = 'o'
        self.inputPath = inputPath

    def getBoard(self, startValue):
        self.grid = {}
        counter = 0
        program = Program1202(self.inputPath)
        initialValue = 2
        while not program.isFinished():
            program.run(initialValue)
            counter += 1
            currentOutput = Operation.getOutput()[0]
            Operation.initializeOutput()

            if currentOutput == 0:
                if initialValue == 1:
                    if str(self.currentX) + " " + str(self.currentY - 1) not in self.grid:
                        self.grid[str(self.currentX) + " " + str(self.currentY - 1)] = {}
                        self.grid[str(self.currentX) + " " + str(self.currentY - 1)]['tile'] = '#'
                        self.grid[str(self.currentX) + " " + str(self.currentY - 1)]['visit'] = 1000
                elif initialValue == 2:
                    if str(self.currentX) + " " + str(self.currentY + 1) not in self.grid:
                        self.grid[str(self.currentX) + " " + str(self.currentY + 1)] = {}
                        self.grid[str(self.currentX) + " " + str(self.currentY + 1)]['tile'] = '#'
                        self.grid[str(self.currentX) + " " + str(self.currentY + 1)]['visit'] = 1000
                elif initialValue == 3:
                    if str(self.currentX - 1) + " " + str(self.currentY) not in self.grid:
                        self.grid[str(self.currentX - 1) + " " + str(self.currentY)] = {}
                        self.grid[str(self.currentX - 1) + " " + str(self.currentY)]['tile'] = '#'
                        self.grid[str(self.currentX - 1) + " " + str(self.currentY)]['visit'] = 1000
                elif initialValue == 4:
                    if str(self.currentX + 1) + " " + str(self.currentY) not in self.grid:
                        self.grid[str(self.currentX + 1) + " " + str(self.currentY)] = {}
                        self.grid[str(self.currentX + 1) + " " + str(self.currentY)]['tile'] = '#'
                        self.grid[str(self.currentX + 1) + " " + str(self.currentY)]['visit'] = 1000
                initialValue = self.getNextValue()
            elif currentOutput == 1:
                if str(self.currentX) + " " + str(self.currentY) in self.grid:
                    if (self.currentX == 25 and self.currentY == 22):
                        self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = 'X'
                    else:
                        self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = '.'
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['visit'] += 1
                else:
                    self.grid[str(self.currentX) + " " + str(self.currentY)] = {}
                    if (self.currentX == 25 and self.currentY == 22):
                        self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = 'X'
                    else:
                        self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = '.'
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['visit'] = 1
                if initialValue == 1:
                    self.currentY -= 1
                elif initialValue == 2:
                    self.currentY += 1
                elif initialValue == 3:
                    self.currentX -= 1
                elif initialValue == 4:
                    self.currentX += 1
                if str(self.currentX) + " " + str(self.currentY) not in self.grid:
                    self.grid[str(self.currentX) + " " + str(self.currentY)] = {}
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = 'D'
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['visit'] = 1
                else:
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = 'D'
                    self.grid[str(self.currentX) + " " + str(self.currentY)]['visit'] += 1
                initialValue = self.getNextValue()
            elif currentOutput == 2:
                self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = '.'
                if initialValue == 1:
                    self.currentY -= 1
                elif initialValue == 2:
                    self.currentY += 1
                elif initialValue == 3:
                    self.currentX -= 1
                elif initialValue == 4:
                    self.currentX += 1
                self.grid[str(self.currentX) + " " + str(self.currentY)] = {}
                self.grid[str(self.currentX) + " " + str(self.currentY)]['tile'] = 'O'
                self.grid[str(25) + " " + str(22)]['tile'] = 'X'
                #self.printBoard()
                with open('data.txt', 'w') as outfile:
                    json.dump(self.grid, outfile)
                self.min_dist = 10000
                self.getShortestPath(25, 22, self.currentX, self.currentY, {}, 0)
                print(self.min_dist)
                return

    def getShortestPath(self, startX, startY, oxygenBoardX, oxygenBoardY, visited, dist):
        if self.grid == {}:
            with open('data.txt') as json_file:
                self.grid = json.load(json_file)

        if (startX == oxygenBoardX and startY == oxygenBoardY):
            self.min_dist = min(dist, self.min_dist)
            return

	#set (startX, startY) cell as visited
        if startY in visited:
            visited[startY][startX] = 1
        else:
            visited[startY] = {}
            visited[startY][startX] = 1
	 
        #go to bottom cell
        if self.isValid(startX + 1, startY, visited):
            self.getShortestPath(startX + 1, startY, oxygenBoardX, oxygenBoardY, visited, dist + 1);
 
	#go to right cell		 
        if self.isValid(startX, startY + 1, visited):
            self.getShortestPath(startX, startY + 1, oxygenBoardX, oxygenBoardY, visited, dist + 1);
	 
	#go to top cell
        if self.isValid(startX - 1, startY, visited):
            self.getShortestPath(startX - 1, startY, oxygenBoardX, oxygenBoardY, visited, dist + 1);
	 
	#go to left cell
        if self.isValid(startX, startY - 1, visited):
            self.getShortestPath(startX, startY - 1, oxygenBoardX, oxygenBoardY, visited, dist + 1);
	 
        # Backtrack - Remove (startX, startY) from visited matrix
        visited[startY][startX] = 0;

    def isValid(self, x, y, visited):
        if str(x) + " " + str(y) not in self.grid:
            return False
        if y not in visited:
            visited[y] = {}
            visited[y][x] = False
        else:
            if x not in visited[y]:
                visited[y][x] = False
            
        if self.grid[str(x) + " " + str(y)]['tile'] == '#' or visited[y][x]:
            return False
        return True
            
    def getNextValue(self):
        if str(self.currentX) + " " + str(self.currentY - 1) not in self.grid:
            return 1
        elif str(self.currentX) + " " + str(self.currentY + 1) not in self.grid:
            return 2
        elif str(self.currentX - 1) + " " + str(self.currentY) not in self.grid:
            return 3
        elif str(self.currentX + 1) + " " + str(self.currentY) not in self.grid:
            return 4

        minVisits = 10000
        minVisitDrection = 0
        if self.grid[str(self.currentX) + " " + str(self.currentY - 1)]['tile'] != '#':
            visits = self.grid[str(self.currentX) + " " + str(self.currentY - 1)]['visit']
            if visits < minVisits:
                minVisits = visits
                minVisitDirection = 1
        if self.grid[str(self.currentX) + " " + str(self.currentY + 1)]['tile'] != '#':
            visits = self.grid[str(self.currentX) + " " + str(self.currentY + 1)]['visit']
            if visits < minVisits:
                minVisits = visits
                minVisitDirection = 2
        if self.grid[str(self.currentX - 1) + " " + str(self.currentY)]['tile'] != '#':
            visits = self.grid[str(self.currentX - 1) + " " + str(self.currentY)]['visit']
            if visits < minVisits:
                minVisits = visits
                minVisitDirection = 3
        if self.grid[str(self.currentX + 1) + " " + str(self.currentY)]['tile'] != '#':
            visits = self.grid[str(self.currentX + 1) + " " + str(self.currentY)]['visit']
            if visits < minVisits:
                minVisits = visits
                minVisitDirection = 4
        return minVisitDirection

    def printBoard(self):
        os.system("cls")
        minX = 0
        minY = 0
        maxX = -100
        maxY = -100    

        for coordinates in self.grid:
            [x, y] = coordinates.split(" ")
            x = int(x)
            y = int(y)
            if x < minX:
                minX = x
            if y < minY:
                minY = y
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y

        self.xDim = maxX - minX + 1
        self.yDim = maxY - minY + 1

        signLetters = []
        for i in range(0, self.yDim):
            signLetters.append([' '] * self.xDim)

        for coordinates in self.grid:
            [x, y] = coordinates.split()
            x = int(x) - minX
            y = int(y) - minY 
    
            tileId = self.grid[coordinates]['tile']
            signLetters[y][x] = tileId
            
        board = ''
        for i in range(0, self.yDim):
            board += ''.join(signLetters[i]) + "\n"

        print(board)

    
                

inputPath = 'InputDay15.txt'

robot = OxygenSystem(inputPath)

robot.getBoard(0)
