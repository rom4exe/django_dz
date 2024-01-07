from django.shortcuts import render, reverse


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
    'burger': {
            'булка сдобная, (располовиненая повдоль)': 1,
            'котлета, целая': 1,
            'сыр, ломтик': 2,
            'помидор, ломтик': 3,
            'салат зелёный, лист': 2,
    },
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
def main_page(request):
    context = {'pages': DATA}
    return render(request, 'calculator/main.html', context)

def recipes(request):
    i = request.get_full_path()[1:].partition('/')[0]
    s = int(request.GET.get("servings", 1))
    count = {}
    if DATA.get(i,''):
        for ingredient, amount in DATA.get(i,'').items():
            count[ingredient] = amount*s
    context = {'recipe': count}
    return render(request, 'calculator/index.html', context)

def page_not_found_view(request, exception):
    return render(request, 'calculator/index.html', status=404)