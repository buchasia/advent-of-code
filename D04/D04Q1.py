def countTrees(inputPath, requiredFields):

    totalValid = 0
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    currentFields = []
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")
        
        if valueLine == "":
            totalValid += checkFields(currentFields, requiredFields)
            currentFields = []
            continue
        
        keyValuePairs = valueLine.split(" ")
        for keyValue in keyValuePairs:
            [key, value] = keyValue.split(":")
            currentFields.append(key)

    totalValid += checkFields(currentFields, requiredFields)
    
    return totalValid

def checkFields(currentFields, requiredFields):
    for field in requiredFields:
        if field not in currentFields:
            return 0

    return 1


print(countTrees('InputD04Q1.txt', ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))
