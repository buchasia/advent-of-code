import re

def countTrees(inputPath, requiredFields):

    totalValid = 0
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    currentFields = {}
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")
        
        if valueLine == "":
            totalValid += checkFields(currentFields, requiredFields)
            currentFields = {}
            continue
        
        keyValuePairs = valueLine.split(" ")
        for keyValue in keyValuePairs:
            [key, value] = keyValue.split(":")
            currentFields[key] = value

    totalValid += checkFields(currentFields, requiredFields)
    
    return totalValid

def checkFields(currentFields, requiredFields):
    for field in requiredFields:
        if field not in currentFields:
            return 0

        if field == 'byr':
            birthDate = int(currentFields[field])
            if birthDate < 1920 or birthDate > 2002:
                return 0
        elif field == 'iyr':
            issueDate = int(currentFields[field])
            if issueDate < 2010 or issueDate > 2020:
                return 0
        elif field == 'eyr':
            expiryDate = int(currentFields[field])
            if expiryDate < 2020 or expiryDate > 2030:
                return 0
        elif field == 'hgt':
            if len(currentFields[field]) <= 2:
                return 0
            heightUnit = currentFields[field][-2:]
            height = int(currentFields[field][:-2])
            if heightUnit == 'cm':
                if height < 150 or height > 193:
                    return 0
            elif heightUnit == 'in':
                if height < 59 or height > 76:
                    return 0    
        elif field == 'hcl':
            hairColor = currentFields[field]
            if not re.search('^#[0-9a-f]{6}$', hairColor):
                return 0
        elif field == 'ecl':
            eyeColor = currentFields[field]
            if eyeColor not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return 0
        elif field == 'pid':
            passportId = currentFields[field]
            if not re.search('^[0-9]{9}$', passportId):
                return 0
        else:
            return 0
    return 1


print(countTrees('InputD04Q2.txt', ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))
