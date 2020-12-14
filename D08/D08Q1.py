def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    screenW = 50
    screenH = 6

    screen = []
    for h in range(screenH):
        screenLine = []
        for w in range(screenW):
            screenLine.append('.')
        screen.append(screenLine)

    for line in fileLines:
        line = line.strip('\n')
        if line[:4] == 'rect':
            [command, area] = line.split(' ')
            [width, height] = list(map(int, area.split('x')))
            for h in range(height):
                for w in range(width):
                    screen[h][w] = '#'
        else:
            data = line.split(' ')
            if data[1] == 'row':
                h = int(data[2][2:])
                shift = int(data[4])
                screenLine = []
                for i in range(screenW - shift, screenW):
                    screenLine.append(screen[h][i])
                for i in range(screenW - shift):
                    screenLine.append(screen[h][i])
                screen[h] = screenLine
            elif data[1] == 'column':
                w = int(data[2][2:])
                shift = int(data[4])
                screenLine = []
                for i in range(screenH - shift, screenH):
                    screenLine.append(screen[i][w])
                for i in range(screenH - shift):
                    screenLine.append(screen[i][w])
                for h in range(screenH):
                    screen[h][w] = screenLine[h]
    counter = 0
    for h in range(screenH):
        for w in range(screenW):
            if screen[h][w] == '#':
                counter += 1

    return counter

print(solveQuestion('InputD08Q1.txt'))
