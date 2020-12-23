def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    layers = {}
    for line in fileLines:
        [layer, rangeLayer] = line.strip().split(': ')
        layer = int(layer)
        rangeLayer = int(rangeLayer)

        layers[layer] = rangeLayer

    maxLayers = max(list(layers.keys()))

    time = 0
    total = 0
    for layer in range(maxLayers + 1):
        if layer not in layers:
            continue
        if layer % (2* layers[layer] - 2) == 0:
            total += layer * layers[layer]
    return total
    
print(solveQuestion('InputD13Q1.txt'))
