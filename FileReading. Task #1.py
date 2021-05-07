#Сразу определим функцию для записи строки ингридиентов в нужном нам виде
# результатом которой будет словарь
def func_split_dish(line):
    x = line.split('|')
    dict = {}
    dict['ingridient_name'] = x[0].strip()
    dict['quantity'] = x[1].strip()
    dict['measure'] = x[2].strip()
    return dict

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    # первая строка файла - блюдо
    dish = file.readline().strip()
    # создадим словарь cook_book с ключом из первой строки файла
    cook_book[dish] = []
    # цикл по остальным строкам файла
    for line in file:
        # символ | говорит о том, что в строке идет речь об ингридиентах
        if '|' in line.strip():
            cook_book[dish].append(func_split_dish(line.strip()))
        # если строка пустая, значит в файле начинается перечисление ингр-ов нового блюда
        elif line.strip() == '':
            dish = file.readline().strip()
            cook_book[dish] = []


print(*cook_book.items(), sep = '\n')