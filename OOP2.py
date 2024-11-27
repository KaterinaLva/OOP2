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