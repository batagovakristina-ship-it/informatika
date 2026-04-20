list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# определим индекс середины
middle = len(list_players) // 2
# разделим на две равные команды
one = list_players[:middle]
two = list_players[middle:]
# распечатаем каждую команду в отдельной строке
print(one)
print(two)
