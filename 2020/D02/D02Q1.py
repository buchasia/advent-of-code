def checkPolicy(inputPath):

    totalValid = 0
    
    # Open file for reading module mass data
    with open(inputPath) as fileP:

        # Read the first policy and password to check
        valueLine = fileP.readline()

        # Do this until there is a line to check
        while valueLine:

            [policy, policyChar, password] = valueLine.split(' ')
            policyChar = policyChar[0]

            [minCount, maxCount] = policy.split('-')

            minCount = int(minCount)
            maxCount = int(maxCount)
            count = 0
            
            for character in password:
                if character == policyChar:
                    count += 1

            if count <= maxCount and count >= minCount:
                totalValid += 1
            
            valueLine = fileP.readline()

    return totalValid

print(checkPolicy('InputD02Q1.txt'))
