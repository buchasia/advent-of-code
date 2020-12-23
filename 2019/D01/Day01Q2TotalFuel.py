import math

# In this method we compute total fuel requirement including
# the requirement for carrying fuel for each module

def totalFuel(inputPath):

    # Open file for reading module mass data
    with open(inputPath) as fileP:

        # Read mass for first module
        valueLine = fileP.readline()

        # empty lines can be ignored
        if valueLine != '':
            mass = int(valueLine)

        # Initialize total fuel
        totalFuel = 0

        # Do this until there is a module mass in the file
        while valueLine:

            # compute the required fule per line
            currentFuel = math.floor(mass / 3) - 2

            # Following computes the fuel required to
            # carry the fuel itself for this module
            while currentFuel > 0:
                totalFuel += currentFuel
                currentFuel = math.floor(currentFuel / 3) - 2
                
            # Read the next line
            valueLine = fileP.readline()

            # empty lines can be ignored
            if valueLine != '':
                mass = int(valueLine)
            
    return totalFuel

print(totalFuel('InputDay01Q2.txt'))
