book = {'Oleg':991155, 'Yurii':182364}
new_book = {}

for key, val in book.items():
    new_book[str(val)] = key

print("Старый словарь: ", book)
print("Новый словарь: ", new_book)