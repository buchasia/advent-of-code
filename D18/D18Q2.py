from pythonds.basic import Stack

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    total = 0
    for line in fileLines:
        line = line.replace('(', '( ')
        line = line.replace(')', ' )')

        total += postfixEvaluate(infixToPostfix(line))
    return total

def postfixEvaluate(expression):
    operations = Stack()
    tokens = expression.split()

    for token in tokens:
        if token in "0123456789":
            operations.push(int(token))
        else:
            operand2 = operations.pop()
            operand1 = operations.pop()
            if token == '*':
                result = operand1 * operand2
            else:
                result = operand1 + operand2
            operations.push(result)
    return operations.pop()
        
def infixToPostfix(infixexpr):
    precedence = {}
    precedence["*"] = 2
    precedence["+"] = 3
    precedence["("] = 1
    operations = Stack()
    result = []
    tokens = infixexpr.split()

    for token in tokens:
        if token in "0123456789":
            result.append(token)
        elif token == '(':
            operations.push(token)
        elif token == ')':
            topToken = operations.pop()
            while topToken != '(':
                result.append(topToken)
                topToken = operations.pop()
        else:
            while (not operations.isEmpty()) and precedence[operations.peek()] >= precedence[token]:
                  result.append(operations.pop())
            operations.push(token)

    while not operations.isEmpty():
        result.append(operations.pop())
    return " ".join(result)

print(solveQuestion('InputD18Q1.txt'))
