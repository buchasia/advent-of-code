from collections import Counter

def getAllData(inputPath):

    # Open file for reading directions
    with open(inputPath) as fileP:

        valueLine = fileP.readline().strip()
        stringValues = []

        while valueLine:
            stringValues.append(valueLine)
            valueLine = fileP.readline().strip()

    return stringValues

def getValues(stringValues):
    values = {}
    for stringValue in stringValues:
        count = 0
        for digit in stringValue:
            if count in values:
                values[count].append(int(digit))
            else:
                values[count] = [int(digit)]

            count += 1

    return values
            
def getDecimal(inputData):
    resultLow = ''
    resultHigh = ''
    values = getValues(inputData)
    for key in values:
        counts = Counter(values[key])
        if counts[0] > counts[1]:
            resultHigh += '0'
            resultLow += '1'
        else:
            resultHigh += '1'
            resultLow += '0'
        
    return int(resultLow, 2) * int(resultHigh, 2)

def getBitCriterion(inputData):
    stringValuesHigh = list(inputData)
    stringValuesLow = list(inputData)
    values = getValues(inputData)
    for key in values.keys():
        valuesHigh = getValues(stringValuesHigh)
        valuesLow = getValues(stringValuesLow)
        countsHigh = Counter(valuesHigh[key])
        countsLow  = Counter(valuesLow[key])
        if countsHigh[0] == countsHigh[1]:
            if len(stringValuesHigh) > 1:
                stringValuesHigh = list(filter(lambda stringValue: stringValue[key] == '1' , stringValuesHigh))
        elif countsHigh[0] < countsHigh[1]:
            if len(stringValuesHigh) > 1:
                stringValuesHigh = list(filter(lambda stringValue: stringValue[key] == '1' , stringValuesHigh))
        elif countsHigh[0] > countsHigh[1]:
            if len(stringValuesHigh) > 1:
                stringValuesHigh = list(filter(lambda stringValue: stringValue[key] == '0' , stringValuesHigh))

        if countsLow[0] == countsLow[1]:
            if len(stringValuesLow) > 1:    
                stringValuesLow = list(filter(lambda stringValue: stringValue[key] == '0' , stringValuesLow))            
        elif countsLow[0] < countsLow[1]:
            if len(stringValuesLow) > 1:
                stringValuesLow = list(filter(lambda stringValue: stringValue[key] == '0' , stringValuesLow))
        elif countsLow[0] > countsLow[1]:
            if len(stringValuesLow) > 1:
                stringValuesLow = list(filter(lambda stringValue: stringValue[key] == '1' , stringValuesLow))

    return int(stringValuesHigh[0], 2) * int(stringValuesLow[0], 2)                


# Part 1
print('Part 1:', getDecimal(getAllData('Input.txt')))

# Part 2
print('Part 2:', getBitCriterion(getAllData('Input.txt')))
