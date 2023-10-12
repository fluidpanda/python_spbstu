symbol = 4
row = symbol * 25
page = row * 50
pages = page * 100
data_set = 1.44 * 1024 * 1024
books = int(data_set // pages)

print("Количество книг, помещающихся на дискету:", books)
