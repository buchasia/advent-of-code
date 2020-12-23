def getAllBridges(components, bridge = [], seen= set(), bridges={}):
    if len(seen) == len(components):
        return [bridge, bridges]

    for index in range(len(components)):
        if index in seen:
            continue

        if bridge[-1][1] in components[index]:
            seen.add(index)
            newBridge = list(bridge)
            newBridge.append((bridge[-1][1], sum(components[index])- bridge[-1][1]))

            [finalBridge, bridges] = getAllBridges(components, newBridge, seen)

            seen.remove(index)

            bridgeText = ''.join([str(comp[0]) + '/' + str(comp[1]) + '-' for comp in finalBridge])
            bridgeText = bridgeText[:-1]
            bridges[bridgeText] = sum([comp[0] + comp[1] for comp in finalBridge])

    return [bridge, bridges]

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    components = []
    
    for line in fileLines:
        [first, second] = list(map(int, line.strip().split('/')))
        components.append((first, second))

    [_, allBridges] = getAllBridges(components, [(0, 0)])

    maxValue = 0
    maxBridgeComponent = 0
    maxBridgeComponentValue = 0
    for bridge in allBridges:
        if allBridges[bridge] > maxValue:
            maxValue = allBridges[bridge]
        if bridge.count('-') > maxBridgeComponent:
            maxBridgeComponent = bridge.count('-')
            maxBridgeComponentValue = allBridges[bridge]
        elif bridge.count('-') == maxBridgeComponent:
            if maxBridgeComponentValue < allBridges[bridge]:
                maxBridgeComponentValue = allBridges[bridge]

    return [maxValue, maxBridgeComponentValue]

    
print(solveQuestion('InputD24.txt'))
