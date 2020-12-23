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

    time = -1
    while 1:
        time += 1
        total = 0
        caught = False
        for layer in range(maxLayers + 1):
            if layer not in layers:
                continue
            if (time + layer) % (2 * layers[layer] - 2) == 0:
                caught = True
                break

        if not caught:
            return time
    
print(solveQuestion('InputD13Q2.txt'))
