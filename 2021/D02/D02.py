import math

def getAllData(inputPath):

    directions = {}

    count = 0
    
    # Open file for reading directions
    with open(inputPath) as fileP:

        valueLine = fileP.readline()

        while valueLine:

            directions[count] = {}
            
            [direction, movement] = valueLine.split(' ')
        
            if direction == 'forward':
                directions[count][direction] = int(movement)
            elif direction == 'down':
                directions[count]['depth'] = int(movement)
            elif direction == 'up':
                directions[count]['depth'] = -1 * int(movement)

            valueLine = fileP.readline()

            count += 1
            
    return directions
            

def getPosition(directions, workWithAim):

    x = 0
    y = 0
    a = 0
    
    # loop over the directions
    for steps in directions:
        for key in directions[steps]:
            if key == 'forward':
                x += directions[steps][key]
                y += directions[steps][key] * workWithAim * a
            else:
                y += (1 - workWithAim) * directions[steps][key]
                a += directions[steps][key]
        
    return x * y

# Part 1
print('Part 1:', getPosition(getAllData('Input.txt'), 0))

# Part 2
print('Part 2:', getPosition(getAllData('Input.txt'), 1))
