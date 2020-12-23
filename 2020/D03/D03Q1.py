def countTrees(inputPath):

    totalTrees = 0
    terrain = []

    widthRepeat = 0
    heightRepeat = 0
    
    # Open file for reading the terrain
    with open(inputPath) as fileP:

        valueLine = str(fileP.readline()).rstrip("\n")

        widthRepeat = len(valueLine);
        
        while valueLine:
            heightRepeat += 1
            terrain.append(valueLine)
            valueLine = str(fileP.readline()).rstrip("\n")

    currentHeight = 0
    currentWidth = 0

    print(terrain)
    
    while currentHeight < heightRepeat - 1:
        currentHeight += 1
        currentWidth += 3
        if currentWidth >= widthRepeat:
            currentWidth %= widthRepeat

        if terrain[currentHeight][currentWidth] == '#':
            totalTrees += 1
    
    return totalTrees


print(countTrees('InputD03Q1.txt'))
