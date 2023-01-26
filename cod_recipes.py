import os
with open('recipes.txt', 'rt') as r:
    cook_book = {}
    recipe_dictionary = []
    for i in r:
        dish_name = i.strip()
        dish_counter = int(r.readline())
        ingredients = []
        #recipe_dictionary.append(dish_name)
        for i in range(r):
            dish = dish_counter.readline()
            ingredient_name, quantity, measure = dish
            ingredients = append({ingredient_name: ingredient_name, 
            quantity: quantity,
            measure: measure})
            print(ingredients)

   
