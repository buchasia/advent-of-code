class Point:
    def __init__(self, x, y, centralPort = False):
        if centralPort == False and x == 0 and y == 0:
            raise Exception('WrongEndCoordinate', 'Cannot come back to central port')
        self.x = x
        self.y = y

    def moveLeft(self, leftBy):
        return Point(self.x - leftBy, self.y)

    def moveRight(self, rightBy):
        return Point(self.x + rightBy, self.y)

    def moveUp(self, upBy):
        return Point(self.x, self.y + upBy)

    def moveDown(self, downBy):
        return Point(self.x, self.y - downBy)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def print(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

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
    def doIntersect(firstStart, firstEnd, secondStart, secondEnd):
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
                    return [True, abs(firstStart.getX()) + abs(secondStart.getY())]
                else:
                    return [False, 0]
            else:
                return [False, 0]
        else:
            if ((firstStart.getY() < secondEnd.getY() and firstStart.getY() > secondStart.getY()) or
                (firstStart.getY() > secondEnd.getY() and firstStart.getY() < secondStart.getY())):
                if ((secondStart.getX() < firstEnd.getX() and secondStart.getX() > firstStart.getX()) or
                    (secondStart.getX() > firstEnd.getX() and secondStart.getX() < firstStart.getX())):
                    return [True, abs(firstStart.getY()) + abs(secondStart.getX())]
                else:
                    return [False, 0]
            else:
                return [False, 0]
