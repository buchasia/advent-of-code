import math

# In this method we compute total fuel requirement for modules

def totalFuel(inputPath):

    # Open file for reading module mass data
    with open(inputPath) as fileP:

        # Read mass data for first module
        valueLine = fileP.readline()

        # empty lines can be ignored
        if valueLine != '':
            mass = int(valueLine)

        # Initialize total fuel
        totalFuel = 0

        # Do this until there is a module mass in the file
        while valueLine:

            # compute the required fule per module mass
            totalFuel += math.floor(mass / 3) - 2

            # Read the mass for the next module
            valueLine = fileP.readline()

            # empty lines can be ignored
            if valueLine != '':
                mass = int(valueLine)
            
    return totalFuel

print(totalFuel('InputDay01Q1.txt'))
