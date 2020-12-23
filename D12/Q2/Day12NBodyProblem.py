from NBody import NBody

nBody = NBody('InputDay12.txt')

nBody.getInitialCoordinates()

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

def computeLCM(x, y):
   # choose the greater number
   lcm = (x * y)//computeGCD(x, y)
   return lcm

xRepeat = nBody.runIteration('x')
yRepeat = nBody.runIteration('y')
zRepeat = nBody.runIteration('z')

print(computeLCM(computeLCM(xRepeat, yRepeat), zRepeat))
