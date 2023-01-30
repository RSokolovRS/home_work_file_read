
with open(r'C:\Users\RSokolov\Desktop\text.txt', mode = 'rt', encoding='utf-8') as t:
    cook_book = {}
    for i in t:
        food_names = i.strip()
        food_counter = int(t.readline().strip())
        food_name = []
        for _ in range(food_counter):
            tx = t.readline().strip().split('|')
            ingredient_name, quantity, measure = tx
            food_name.append({'ingredient_name': ingredient_name, 
                             'quantity': quantity, 
                            'measure': measure})
        t.readline()
        cook_book = {food_names:food_name}
        print(cook_book)