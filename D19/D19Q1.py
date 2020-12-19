def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines= fileP.readlines()
    fileP.close()
    paths = []
    pathAlpha = ''
    for line in fileLines:
        newLine = [char for char in line.strip('\n')]
        paths.append(newLine)

    x = paths[0].index('|')
    y = 0
    direction = 'D'
    alphaFound = False
    while True:
        if direction == 'D':
            y += 1
        elif direction == 'U':
            y -= 1
        elif direction == 'L':
            x -= 1
        elif direction == 'R':
            x += 1

        if paths[y][x] == '+':
            if paths[y][x + 1] == '-' and direction != 'L':
                direction = 'R'
            elif paths[y][x - 1] == '-' and direction != 'R':
                direction = 'L'
            elif paths[y + 1][x] == '|' and direction != 'U':
                direction = 'D'
            elif paths[y - 1][x] == '|' and direction != 'D':
                direction = 'U'
        elif paths[y][x] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pathAlpha += paths[y][x]
            alphaFound = True
            print(pathAlpha)
        elif paths[y][x] == ' ' and alphaFound:
            break
        else:
            alphaFound = False    

    return pathAlpha        
        
print(solveQuestion('InputD19Q1.txt'))
