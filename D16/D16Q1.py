def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    allValues =  []
    total = 0
    isYourTicket = False
    isNearbyTicket = False
    for line in fileLines:
        line = line.strip()
        if line == '':
            if isYourTicket != True:
                isYourTicket = True
            else:
                if isNearbyTicket != True:
                    isNearbyTicket = True
            continue

        if line[:4] == 'your' or line[:6] == 'nearby':
            continue
        if isYourTicket == False and isNearbyTicket == False:
            [field, values] = line.strip().split(': ')
            [valueRange1, valueRange2] = values.split(' or ')
            [min1, max1] = valueRange1.split('-')
            [min2, max2] = valueRange2.split('-')
            for i in range(int(min1), int(max1) + 1):
                if i not in allValues:
                    allValues.append(i)
            for i in range(int(min2), int(max2) + 1):
                if i not in allValues:
                    allValues.append(i)
        elif isYourTicket == True and isNearbyTicket != True:
            yourTicket = list(map(int, line.strip().split(',')))
        elif isYourTicket == True and isNearbyTicket == True:
            values = list(map(int, line.split(',')))
            for value in values:
                if value not in allValues:
                    total += value
    return total
    
print(solveQuestion('InputD16Q1.txt'))
