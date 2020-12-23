def solveProblem(inputPath):

    totalRibbonLength = 0
    
    with open(inputPath) as fileP:

        valueLine = fileP.readline()

        while valueLine:

            valueLine = str(valueLine).strip('\n')
            dimensions = list(map(int, valueLine.split('x')))

            dimensions.sort()

            totalRibbonLength += 2 * dimensions[0] + 2 * dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]
            
            valueLine = fileP.readline()
                
    return totalRibbonLength

print(solveProblem('InputD02Q1.txt'))
