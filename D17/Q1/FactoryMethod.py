from Operation01 import Operation01
from Operation02 import Operation02
from Operation03 import Operation03
from Operation04 import Operation04
from Operation05 import Operation05
from Operation06 import Operation06
from Operation07 import Operation07
from Operation08 import Operation08
from Operation09 import Operation09
from Operation99 import Operation99

def getOperation(opCode):
    if(opCode == 1):
        return Operation01()
    elif(opCode == 2):
        return Operation02()
    elif(opCode == 3):
        return Operation03()
    elif(opCode == 4):
        return Operation04()
    elif(opCode == 5):
        return Operation05()
    elif(opCode == 6):
        return Operation06()
    elif(opCode == 7):
        return Operation07()
    elif(opCode == 8):
        return Operation08()
    elif(opCode == 9):
        return Operation09()
    elif(opCode == 99):
        return Operation99()
    else:
        raise Exception('Operation Invalid')
