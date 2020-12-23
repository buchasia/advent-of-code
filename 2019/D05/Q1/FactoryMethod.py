from Operation01 import Operation01
from Operation02 import Operation02
from Operation03 import Operation03
from Operation04 import Operation04
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
    elif(opCode == 99):
        return Operation99()
    else:
        raise Exception('Operation Invalid')
