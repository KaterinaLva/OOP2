def read_cookbook(file_path):
    cook_book = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            # Чтение названия рецепта
            dish_name = file.readline().strip()
            
            if not dish_name:
                break
                
            # Чтение количества ингредиентов
            num_ingredients = int(file.readline().strip())
            
            # Чтение ингредиентов
            ingredients_list = []
            for _ in range(num_ingredients):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient_name = ingredient_data[0]
                quantity = float(ingredient_data[1])
                measure = ingredient_data[2]
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            
            # Добавляем рецепт в словарь
            cook_book[dish_name] = ingredients_list
            
            # Пропуск пустой строки между рецептами
            file.readline()
    
    return cook_book


# Ф-ция принимает список блюд, кол-во персон, кулинарную книгу. 
# Рассчитывает общее количество ингредиентов для приготовляемых блюд
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list