import timeit
import copy

# This class will handle each node in the doubly linked list
class Node(object):
    def __init__(self, valueCurrentNode, previousNode, nextNode, parentList):
        self.parentList = parentList
        self.value = valueCurrentNode
        self.previous = previousNode
        self.next = nextNode
    def insert(self, valueToInsert):
        node = Node(valueToInsert, self, self.next, self.parentList)
        self.parentList.Nodes[valueToInsert] = node
        self.next = node
        node.next.previous = node
        return node
    def erase(self):
        self.next.previous = self.previous
        self.previous.next = self.next
        del self.parentList.Nodes[self.value]

class DoubleLinkedList(object):
    def __init__(self):
        self.Nodes = {}
    def append(self, previousNode, valueToAppend):
        if previousNode is None:
            node = Node(valueToAppend, None, None, self)
            node.next = node
            node.previous = node
            self.Nodes[valueToAppend] = node
        else:
            node = Node(valueToAppend, previousNode, previousNode.next, self)
            previousNode.next = node
            node.next.previous = node
            self.Nodes[valueToAppend] = node
        return node

    def find(self, valueToFind):
        return self.Nodes[valueToFind]

def solveParts(startSequence, nMoves = 100):

    maxDestination = int(max(list(startSequence))) if nMoves == 100 else nMoves // 10
    
    DDL = DoubleLinkedList()
    previousNode = None
    for digit in startSequence:
        previousNode = DDL.append(previousNode, int(digit))

    if nMoves != 100:
        for i in range(10, 1000001):
            previousNode = DDL.append(previousNode, i)

    currentCupNode = DDL.find(int(startSequence[0])).previous
    for i in range(nMoves):
        currentCupNode = currentCupNode.next
        
        pickUp = []
        for j in range(3):
            pickUp.append(currentCupNode.next.value)
            currentCupNode.next.erase()

        destination = currentCupNode.value - 1 if currentCupNode.value > 1 else maxDestination
        while destination in pickUp:
            destination = destination - 1 if destination > 1 else maxDestination

        destinationNode = DDL.find(destination)
        for j in range(3):
            destinationNode.insert(pickUp[2 - j])

    node = DDL.find(1)

    if nMoves == 100:
        string = ''
        for j in range(len(startSequence) - 1):
            string += str(node.next.value)
            node = node.next
        return string
    else:
        return node.next.value * node.next.next.value
        
def solve(startSequence):
    print([solveParts(startSequence),
           solveParts(startSequence, nMoves = 10000000)])

#Timer Start
start = timeit.default_timer()

solve('123487596')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
