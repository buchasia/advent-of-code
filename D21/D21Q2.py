import json
def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    allergyIngredient = {}
    ingredientsCount = {}
    for line in fileLines:
        line = line.strip()
        [ingredients, allergies] = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergies = allergies[:-1].split(', ')
        for ingredient in ingredients:
            if ingredient in ingredientsCount:
                ingredientsCount[ingredient] += 1
            else:
                ingredientsCount[ingredient] = 1
        for allergy in allergies:
            if allergy not in allergyIngredient:
                allergyIngredient[allergy] = {}
                for ingredient in ingredients:
                    if ingredient in allergyIngredient[allergy]:
                        allergyIngredient[allergy][ingredient] += 1
                    else:
                        allergyIngredient[allergy][ingredient] = 1
            else:
                for ingredient in ingredients:
                    if ingredient in allergyIngredient[allergy]:
                        allergyIngredient[allergy][ingredient] += 1
                    else:
                        allergyIngredient[allergy][ingredient] = 1

    confirmedAllergyMax = {}
    for allergy in allergyIngredient:
        maxCount = 0
        for ingredient in allergyIngredient[allergy]:
            if allergyIngredient[allergy][ingredient] > maxCount:
                maxCount = allergyIngredient[allergy][ingredient]

        confirmedAllergyMax[allergy] = maxCount

    confirmedAllergy = {}
    for allergy in allergyIngredient:
        confirmedAllergy[allergy] = []
        for ingredient in allergyIngredient[allergy]:
            if allergyIngredient[allergy][ingredient] == confirmedAllergyMax[allergy]:
                confirmedAllergy[allergy].append(ingredient)

    matchFound = {}
    while len(matchFound) != len(confirmedAllergy):
        for allergy in confirmedAllergy:
            if len(confirmedAllergy[allergy]) == 1:
                matchFound[allergy] = confirmedAllergy[allergy][0]
            else:
                for matchAllergy in matchFound:
                    if matchFound[matchAllergy] in confirmedAllergy[allergy]:
                        confirmedAllergy[allergy].remove(matchFound[matchAllergy])
    output = ''
    for allergy in sorted(matchFound.keys()):
        output += ',' + matchFound[allergy]

    return output[1:]
    
print(solveQuestion('InputD21Q2.txt'))
