# In this method we implement Universal Orbit Map
from UniversalOrbitMap import UniversalOrbitMap

uOMap = UniversalOrbitMap()

inputPath = 'InputDay06Q2.txt'

with open(inputPath) as fileP:
    # Read the first orbit data
    valueLine = fileP.readline().strip()
    while valueLine:
        [around, orbiter] = valueLine.split(')')
        uOMap.addToMap(around, orbiter)
        valueLine = fileP.readline().strip()


#print(uOMap.getOrbitMap())
print(uOMap.getNumberOfOrbitalTransfer('YOU', 'SAN')[2])
    

    
