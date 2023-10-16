symbol: int = 4
row: int = symbol * 25
page: int = row * 50
pages: int = page * 100
data_set: int = 1.44 * 1024 * 1024
books = int(data_set // pages)

print("Количество книг, помещающихся на дискету:", books)
