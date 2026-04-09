# TODO Напишите функцию для поиска индекса товара
def find_index_item(list, target): #Будет возвращать индекс первого вхождения товара
    for index in range(len(list)): #Рассматриваем все индексы списка
        if list[index] == target:  #Если элемент с данным индексом равен исходному товару - возвращаем данный индекс
            return index
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None: #Проверяем, вернула ли функция None
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.") #Товар найден
    else:
        print(f"Товар '{find_item}' не найден в списке.") #Функция не вернула None - товар не найден

