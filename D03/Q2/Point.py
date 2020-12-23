class Point:
    def __init__(self, x, y, stepCount, centralPort = False):
        if centralPort == False and x == 0 and y == 0:
            raise Exception('WrongEndCoordinate', 'Cannot come back to central port')
        self.x = x
        self.y = y
        self.stepCount = stepCount

    def moveLeft(self, leftBy):
        return Point(self.x - leftBy, self.y, self.stepCount + leftBy)

    def moveRight(self, rightBy):
        return Point(self.x + rightBy, self.y, self.stepCount + rightBy)

    def moveUp(self, upBy):
        return Point(self.x, self.y + upBy, self.stepCount + upBy)

    def moveDown(self, downBy):
        return Point(self.x, self.y - downBy, self.stepCount + downBy)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def print(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def getStepCount(self):
        return self.stepCount

    @staticmethod
    def isVertical(start, end):
        if (start.getX() == end.getX()):
            return True
        else:
            return False
        
    @staticmethod
    def isHorizontal(start, end):
        if(start.getY() == end.getY()):
            return True
        else:
            return False
    
    @staticmethod
    def doIntersectWithStepCount(firstStart, firstEnd, secondStart, secondEnd):
        firstPathVertical = Point.isVertical(firstStart, firstEnd)
        secondPathVertical = Point.isVertical(secondStart, secondEnd)
        
        if ((firstPathVertical and secondPathVertical) or
            (not firstPathVertical and not secondPathVertical)):
            return [False, 0]

        if firstPathVertical:
            if ((firstStart.getX() < secondEnd.getX() and firstStart.getX() > secondStart.getX()) or
                (firstStart.getX() > secondEnd.getX() and firstStart.getX() < secondStart.getX())):
                if ((secondStart.getY() < firstEnd.getY() and secondStart.getY() > firstStart.getY()) or
                    (secondStart.getY() > firstEnd.getY() and secondStart.getY() < firstStart.getY())):
                    totalSteps = firstStart.getStepCount() + secondStart.getStepCount()
                    if (firstStart.getY() > firstEnd.getY()):
                        #        v fs -
                        #        v    |
                        #     se x ss -
                        #        v    
                        #        v fe
                        stepY = firstStart.getY() - secondStart.getY()
                    else:
                        #        ^ fe
                        #        ^
                        #     se x ss -
                        #        ^    |
                        #        ^ fs -
                        stepY = secondStart.getY() - firstStart.getY()
                    if (secondStart.getX() > secondEnd.getX()):
                        # se          ss
                        # < < < x < < <
                        #       fs
                        #       fe
                        #        |- - |
                        stepX = secondStart.getX() - firstStart.getX()
                    else:
                        # ss          se
                        # > > > x > > >
                        #       fs
                        #       fe
                        # | - - |
                        stepX = firstStart.getX() - secondStart.getX()
                    totalSteps += stepX + stepY
                    return [True, Point(firstStart.getX(), secondStart.getY(), totalSteps)]
                else:
                    return [False, 0]
            else:
                return [False, 0]
        else:
            if ((firstStart.getY() < secondEnd.getY() and firstStart.getY() > secondStart.getY()) or
                (firstStart.getY() > secondEnd.getY() and firstStart.getY() < secondStart.getY())):
                if ((secondStart.getX() < firstEnd.getX() and secondStart.getX() > firstStart.getX()) or
                    (secondStart.getX() > firstEnd.getX() and secondStart.getX() < firstStart.getX())):
                    totalSteps = firstStart.getStepCount() + secondStart.getStepCount()
                    if (secondStart.getY() > secondEnd.getY()):
                        #        v ss -
                        #        v    |
                        #     fe x fs -
                        #        v    
                        #        v se
                        stepY = secondStart.getY() - firstStart.getY()
                    else:
                        #        ^ se
                        #        ^
                        #     fe x fs -
                        #        ^    |
                        #        ^ ss -
                        stepY = firstStart.getY() - secondStart.getY()
                    if (firstStart.getX() > firstEnd.getX()):
                        # fe          fs
                        # < < < x < < <
                        #       ss
                        #       se
                        #        |- - |
                        stepX = firstStart.getX() - secondStart.getX()
                    else:
                        # fs          fe
                        # > > > x > > >
                        #       ss
                        #       se
                        # | - - |
                        stepX = secondStart.getX() - firstStart.getX()
                    totalSteps += stepX + stepY
                    return [True, Point(firstStart.getY(), secondStart.getX(), totalSteps)]
                else:
                    return [False, 0]
            else:
                return [False, 0]
