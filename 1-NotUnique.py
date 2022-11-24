int_array = [1, 2, 3, 2, 1, 4, 5, 7, 9, 8, 7, 9]
UniqueCheck = {}

#Проверка на уникальность элементов
for k in int_array:
    if k in UniqueCheck:
        UniqueCheck[k] += 1
    else:
        UniqueCheck[k] = 1

#Отсеивание элементов на основе проверки
for key, val in UniqueCheck.items():
    if(val == 1):
            int_array.remove(key)

print(int_array)