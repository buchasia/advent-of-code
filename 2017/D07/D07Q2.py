def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    bottoms = []
    tops = []
    weights = {}
    towers = {}
    for line in fileLines:
        if line.find('->') != -1:
            [nameWeight, overNames] = line.strip().split('->')
            [name, Weight] = nameWeight.strip().split(' ')
            weights[name] = int(Weight.strip()[1:-1])
            overNames = overNames.strip().split(', ')
            bottoms.append(name)
            towers[name] = overNames
            for overName in overNames:
                tops.append(overName)
        else:
            [name, Weight] = line.strip().split(' ')
            weights[name] = int(Weight.strip()[1:-1])

    for bottom in bottoms:
        if bottom in tops:
            continue

        break

    return getTowersWeigths(towers, weights, bottom, 0)[1]

def getTowersWeigths(towers, weights, bottom, diff):
    weightsCurrent = []
    for tower in towers[bottom]:
        if tower in towers:
            [weight, diff] = getTowersWeigths(towers, weights, tower, diff)
            weightsCurrent.append(weight)
            if diff > 0:
                return [0, diff]
        else:
            weightsCurrent.append(weights[tower])
    if diff > 0:
        return [0, diff]
    
    diff = max(weightsCurrent) - min(weightsCurrent)
    if diff > 0:
        if weightsCurrent.count(max(weightsCurrent)) == 1:
            weightVaraint = weights[towers[bottom][weightsCurrent.index(max(weightsCurrent))]]
            diff = weightVaraint - diff
        else:
            weightVaraint = weights[towers[bottom][weightsCurrent.index(min(weightsCurrent))]]
            diff = weightVaraint + diff
        return [0, diff]
        
    return [sum(weightsCurrent) + weights[bottom], 0]

print(solveQuestion('InputD07Q2.txt'))
