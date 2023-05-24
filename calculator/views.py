from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'penis': {
        'конча':4
    }
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculate_recipe(request, dish_name):
    context = {}
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(dish_name)

    if recipe:
        new_recipe = {}
        for ingredient, amount in recipe.items():
            new_amount = round(amount * servings, 2)
            new_recipe[ingredient] = new_amount

        context['recipe'] = new_recipe
        context['dish_name'] = dish_name
        context['servings'] = servings
    else:
        context['error'] = f"Рецепт \"{dish_name}\" не найден"

    return render(request, 'calculator/index.html', context)