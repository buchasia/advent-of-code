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

            [pos1, pos2] = policy.split('-')

            pos1 = int(pos1) - 1
            pos2 = int(pos2) - 1
            count = 0
            
            if ((password[pos1] == policyChar and password[pos2] != policyChar) or
               (password[pos2] == policyChar and password[pos1] != policyChar)):
                totalValid += 1
            
            valueLine = fileP.readline()

    return totalValid

print(checkPolicy('InputD02Q2.txt'))
