from pythonds.basic import Stack

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    rules = {}
    isRules = True
    givenStrings = []
    
    for line in fileLines:
        line = line.strip()

        if line == "":
            isRules = False
            continue

        if isRules == False:
            givenStrings.append(line)
        
        if isRules == True:
            [ruleNo, ruleCondition] = line.split(': ')
            ruleNo = int(ruleNo)
            if ruleCondition[0] == '"':
                rules[ruleNo] = ruleCondition[1]
            elif ruleCondition.find('|') != -1:
                ruleConditions = ruleCondition.split(' | ')
                rules[ruleNo] = []
                for ruleCond in ruleConditions:
                    if ruleCond.find(' ') == -1:
                        rules[ruleNo].append((int(ruleCond), -1))
                    else:
                        [rule1, rule2] = ruleCond.strip().split()
                        rules[ruleNo].append((int(rule1), int(rule2)))
            elif ruleCondition.find(' ') == -1:
                rules[ruleNo] = []
                rules[ruleNo].append((int(ruleCondition), -1))
            else:
                [rule1, rule2] = ruleCondition.strip().split()
                rules[ruleNo] = []
                rules[ruleNo].append((int(rule1), int(rule2)))

    possibilities = getPossibility(rules)

    total = 0
    print('will check now')
    for string in givenStrings:
        if string in possibilities[0]:
            total += 1

    return total

def getPossibility(rules):
    possibilities = {}
    for index in rules:
        if isinstance(rules[index], str):
            if index not in possibilities:
                possibilities[index] = rules[index]    
    while 1:
        for index in rules:
            if index not in possibilities:
                [possibilities, isF] = allInPossible(rules[index], possibilities, index)
                
        if 0 in possibilities:
            break

    return possibilities

def allInPossible(rules, possibilities, index):
    temp = []
    possibility = []
    for rule in rules:
        stringV = []
        for index2 in rule:
            if index2 == -1:
                continue
            if index2 not in possibilities:
                return [possibilities, False]
            else:
                if len(stringV) == 0:
                    if isinstance(possibilities[index2], str):
                        stringV.append(possibilities[index2])
                    else:
                        stringV = possibilities[index2]
                else:
                    tempString = []
                    for string in stringV:
                        for poss in possibilities[index2]:
                            tempString.append(string + poss)

                    stringV = list(tempString)

        for string in stringV:
            possibility.append(string)
                
        
    possibilities[index] = possibility
    return [possibilities, True]

print(solveQuestion('InputD19Q1.txt'))
