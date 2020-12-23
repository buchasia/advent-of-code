# In this method we implement Program 1202 to get the final
# sequence

import itertools

from Program1202 import Program1202
from Operation import Operation

def Boost(inputPath, initialInput):
    
    program = Program1202(inputPath, initialInput)
    program.run()


# Initial Input for Day 1
#initialInput = 1
#Boost('InputDay09.txt', initialInput)

# Initial Input for Day 2
initialInput = 2
Boost('InputDay09.txt', initialInput)
