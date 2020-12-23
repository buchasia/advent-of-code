def solveQuestion(inputPath, searchBag):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    bagsContent = {}
    searchBags = []
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")
        
        [bagType, contentText] = valueLine.split(' contain ')

        bagType = bagType.split(' bags')
        
        # The content is in the format: 3 pale red bags, 1 clear teal bag.
        # We split with space we will get ['3', 'pale', 'red', 'bags,', '1',...]
        # Then the second, third, 6th, 7th are the bag types
        contents = contentText.split(' ')
        counter = 1
        while counter < len(contents):
            contentName = contents[counter] + ' ' + contents[counter + 1]
            if contents[counter - 1] == 'no':
                counter += 4
                continue
            if bagType[0] not in bagsContent:
                bagsContent[bagType[0]] = {}    
                bagsContent[bagType[0]][contentName] = int(contents[counter - 1])
            else:
                bagsContent[bagType[0]][contentName] = int(contents[counter - 1])
            counter += 4
    
    searchBags = [(searchBag, 1)]
    counter = 0
    totalCount = 0
    while counter < len(searchBags):
        currentBag = searchBags[counter]

        currentMultiplier = currentBag[1]
        currentBagName = currentBag[0]
        
        if currentBagName in bagsContent:
            for bag in bagsContent[currentBag[0]]:
                searchBags.append((bag, bagsContent[currentBag[0]][bag] * currentMultiplier))
                totalCount += bagsContent[currentBag[0]][bag] * currentMultiplier
                
        counter += 1

    return totalCount

print(solveQuestion('InputD07Q2.txt', 'shiny gold'))
