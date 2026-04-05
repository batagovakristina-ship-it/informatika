# TODO импортировать необходимые молули

# Импортируем необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file: #Открываем CSV-файл в режиме 'r'
        # Создаём переменную, которая будет читать CSV. Первая строка файла станет ключами (заголовками столбцов)
        reader = csv.DictReader(csv_file, delimiter=',')
        data = list(reader) #Прееобразуем reader в список словарей, где каждая строка становится словарем

    with open(OUTPUT_FILENAME, 'w') as json_file: #Открываем JSON-файл для в режиме 'w'
        json.dump(data, json_file, indent=4, ensure_ascii=False) #Записываем данные в JSON-формат с отступом, сохраняя символы

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


