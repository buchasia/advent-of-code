def countTreesProduct(inputPath, listPathSlopes):
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

    product = 1
    for slope in listPathSlopes:
        product *= countTrees(terrain, widthRepeat, heightRepeat, slope[0], slope[1])

    return product
    
def countTrees(terrain, widthRepeat, heightRepeat, moveRight, moveDown):
    totalTrees = 0

    currentHeight = 0
    currentWidth = 0
    
    while currentHeight < heightRepeat - moveDown:
        currentHeight += moveDown
        currentWidth += moveRight
        if currentWidth >= widthRepeat:
            currentWidth %= widthRepeat

        if terrain[currentHeight][currentWidth] == '#':
            totalTrees += 1
    
    return totalTrees


print(countTreesProduct('InputD03Q2.txt', [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))
