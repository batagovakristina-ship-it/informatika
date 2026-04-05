# TODO Напишите функцию find_common_participants
    #Функция с разделителем-запятой
def find_common_participants(first_group, second_group, delimiter=","):
    # Разбиваем строку первой и второй группы на множество фамилий
    group1_set = set(first_group.split(delimiter))
    group2_set = set(second_group.split(delimiter))
    # Находим общих участников
    common_set = group1_set.intersection(group2_set)
    # Преобразуем множество в список
    common_list = list(common_set)
    # Сортируем список в алфавитном порядке
    common_list.sort()
    # Возвращаем отсортированный список
    return common_list

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(result)


