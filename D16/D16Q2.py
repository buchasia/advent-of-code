def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    allValues =  {}
    allLegalValues = []
    isYourTicket = False
    isNearbyTicket = False
    nearbyValues = {}
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
            allValues[field] = []
            for i in range(int(min1), int(max1) + 1):
                if i not in allLegalValues:
                    allLegalValues.append(i)
                if i not in allValues[field]:
                    allValues[field].append(i)
            for i in range(int(min2), int(max2) + 1):
                if i not in allLegalValues:
                    allLegalValues.append(i)
                if i not in allValues[field]:
                    allValues[field].append(i)
        elif isYourTicket == True and isNearbyTicket != True:
            yourTicket = list(map(int, line.strip().split(',')))
            counter = 0
            for value in yourTicket:
                if counter not in nearbyValues:
                    nearbyValues[counter] = [ value ]
                counter += 1
        elif isYourTicket == True and isNearbyTicket == True:
            values = list(map(int, line.split(',')))
            counter = 0
            notLegal = False
            for value in values:
                if value not in allLegalValues:
                    notLegal = True
                    break
            if notLegal == True:
                continue
            for value in values:
                nearbyValues[counter].append(value)
                counter += 1
    combination = {}
    for field in allValues:
        for index in nearbyValues:
            notFound = False
            for value in nearbyValues[index]:
                if value not in allValues[field]:
                    notFound = True
                    break

            if notFound == False:
                if field in combination:
                    combination[field].append(index)
                else:
                    combination[field] = [index]
    fieldList = []
    while 1:
        fieldName = ''
        for field in combination:
            if len(combination[field]) == 1 and field not in fieldList:
                valueToRemove = combination[field][0]
                fieldName = field
                fieldList.append(fieldName)    
                break
        if fieldName == '':
            break
        for field in combination:
            if field == fieldName:
                continue
            if valueToRemove in combination[field]:
                combination[field].remove(valueToRemove)                   
               
    total = 1
    for field in combination:
        if field[:9] == 'departure':
            total *= nearbyValues[combination[field][0]][0]
    return total
    
print(solveQuestion('InputD16Q2.txt'))
