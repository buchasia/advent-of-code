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
                
    ingredientAllergy = {}
    for allergy in allergyIngredient:
        for ingredient in allergyIngredient[allergy]:
            if ingredient not in ingredientAllergy:
                ingredientAllergy[ingredient] = []
            if ingredient in confirmedAllergy[allergy]:
                ingredientAllergy[ingredient].append(allergy)
        
    total = 0

    for ingredient in ingredientsCount:
        if len(ingredientAllergy[ingredient]) == 0:
            total += ingredientsCount[ingredient]
    return total

print(solveQuestion('InputD21Q1.txt'))
