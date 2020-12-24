import timeit

# This class will handle each node in the linked list
class Node(object):
    def __init__(self, valueCurrentNode, nextNode):
        self.value = valueCurrentNode
        self.next = nextNode
    
class LinkedList(object):
    def __init__(self):
        self.Nodes = {}
    def append(self, previousNode, valueToAppend):
        node = Node(valueToAppend, None)
        self.Nodes[valueToAppend] = node
        if previousNode is None:
            node.next = node
        else:
            previousNode.next = node
        return node
    def insert(self, insertAtNode, valueToInsert):
        node = self.Nodes[valueToInsert]
        node.next = insertAtNode.next
        insertAtNode.next = node

    def find(self, valueToFind):
        return self.Nodes[valueToFind]

def solveParts(startSequence, nMoves = 100):

    maxDestination = int(max(list(startSequence))) if nMoves == 100 else nMoves // 10
    
    LL = LinkedList()
    previousNode = None
    for digit in startSequence:
        previousNode = LL.append(previousNode, int(digit))

    if nMoves != 100:
        for i in range(10, 1000001):
            previousNode = LL.append(previousNode, i)

    currentCupNode = LL.find(int(startSequence[0]))

    previousNode.next = currentCupNode
    for i in range(nMoves):
        pickUp = []
        for j in [0, 1, 2]:
            pickUp.append(currentCupNode.next.value)
            currentCupNode.next = currentCupNode.next.next

        destination = currentCupNode.value - 1 if currentCupNode.value > 1 else maxDestination
        while destination in pickUp:
            destination = destination - 1 if destination > 1 else maxDestination

        destinationNode = LL.find(destination)
        for j in [0, 1, 2]:
            LL.insert(destinationNode, pickUp[2 - j])

        currentCupNode = currentCupNode.next

    node = LL.find(1)

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
