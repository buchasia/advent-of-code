import math

class SpaceStoichiometry:

    def __init__(self, inputPath):
        self.reactions = {}
        self.filePath = inputPath

    def getReactions(self):
        # Open file for reading the input sequence
        with open(self.filePath) as fileP:
            # Read the complete sequence and remove unwanted characters
            initialSequence = fileP.readline().strip()

            while initialSequence:

                # The sequence as List of integers
                [reactantsString, product]  = initialSequence.split(" => ")

                [quantity, productName] = product.split(" ")

                quantity = int(quantity)

                reactantDict = self.getReactantDict(reactantsString)
            
                self.reactions[productName] = {"quantity": quantity, "reactants": reactantDict}

                initialSequence = fileP.readline().strip()

    def getReactantDict(self, reactantsString):
        reactants = reactantsString.split(", ")
        reactantDict = {}
        for reactant in reactants:
            [quantity, reactantName] = reactant.split(" ")
            reactantDict[reactantName] = {"quantity": int(quantity)}
        return reactantDict

    def getOre(self, amountOfFuel):
        finished = ['FUEL']
        products = self.getReactants(amountOfFuel, 'FUEL')
        while not self.justFuel(products):
            productNames = list(products.keys())
            for productName in productNames:
                if productName == 'ORE':
                    continue

                if self.isDependencyFulfilled(productName, finished):
                    newReactants = self.getReactants(products[productName]["quantity"], productName)
                    
                    for newReactant in newReactants:
                        if newReactant in products:
                            products[newReactant]["quantity"] += newReactants[newReactant]["quantity"]
                        else:
                            products[newReactant] = newReactants[newReactant]
                    products.pop(productName, None)
                    finished.append(productName)
                print(products)
        print(products)

    def isDependencyFulfilled(self, productName, finished):
        dependencies = self.tree[productName]
        for dependency in dependencies:
            if dependency not in finished:
                return False
        return True
        

    def justFuel(self, products):
        for product in products:
            if product != 'ORE':
                return False

        return True

    def getDependencyTree(self):
        self.tree = {}
        toLook = ['ORE']

        while len(toLook) != 0:
            currentReactant = toLook[0]
            toLook.pop(0)
            for reaction in self.reactions:
                for reactant in self.reactions[reaction]["reactants"]:
                    if reactant == currentReactant:
                        if reaction not in toLook:
                            toLook.append(reaction)
                        if currentReactant not in self.tree:
                            self.tree[currentReactant] = []
                            if reaction not in self.tree[currentReactant]:
                                self.tree[currentReactant].append(reaction)
                        else:
                            if reaction not in self.tree[currentReactant]:
                                self.tree[currentReactant].append(reaction)
        print(self.tree)
    
    def getReactants(self, amountOfFuel, productName):        
        fuelReaction = self.reactions[productName]
        reactants = fuelReaction['reactants']
        if amountOfFuel <= fuelReaction['quantity']:
            startingReactants = reactants
        else:
            multiplier = math.ceil(amountOfFuel / fuelReaction['quantity'])
            for reactant in reactants:
                reactants[reactant]["quantity"] *= multiplier
        return reactants

        
    
spaceS = SpaceStoichiometry('InputDay14.txt')
spaceS.getReactions()
spaceS.getDependencyTree()
spaceS.getOre(1)
