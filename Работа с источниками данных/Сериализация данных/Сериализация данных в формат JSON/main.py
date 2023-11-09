import json

filename = 'output.json'
indent = 4  # TODO Подставьте любое целое число
ensure_ascii = False  # TODO Замените на значение True

data = {
    'name': 'John',
    'age': 25,
    'город': 'Нью-Йорк'
}

# Запись данных в файл в формате JSON
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)

# Сериализация данных в строку JSON
json_data = json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
print("Сериализация данных с помощью метода `dumps`:", json_data)

# Чтение данных из файла в формате JSON
with open(filename, encoding="utf-8") as file:
    data = json.load(file)
print("Десериализованные данные из JSON файла в python объект1:", data)

# Десериализация данных из строки JSON
data = json.loads(json_data)
print("Десериализованные данные из JSON файла в python объект2:", data)
