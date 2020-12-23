def solveProblem(inputPath):

    totalArea = 0
    
    with open(inputPath) as fileP:

        valueLine = fileP.readline()

        while valueLine:

            valueLine = str(valueLine).strip('\n')
            dimensions = list(map(int, valueLine.split('x')))

            dimensions.sort()

            totalArea += 3 * dimensions[0] * dimensions[1] + 2 * dimensions[0] * dimensions[2] + 2 * dimensions[1] * dimensions[2]
            
            valueLine = fileP.readline()
                
    return totalArea

print(solveProblem('InputD02Q1.txt'))
