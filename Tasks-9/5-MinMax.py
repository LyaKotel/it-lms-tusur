def min(*arg, key=''):
    def innermin(inarg): #Функция, написанная внутри функции во избежание дубликации кода
        #Определение дальнейших действий в зависимости от ключа
        if( callable(key) and (key != int) ): #Если ключ является функцией (lambda)
            xmin = key(inarg[0])
            kmin = inarg[0]
            for k in inarg:
                if(key(k) < xmin):
                    xmin = key(k)
                    kmin = k
            print(f'Min = {kmin}')
        else: #Если ключ является типом данных
            xmin = inarg[0]
            for k in inarg:
                if( (k < xmin) and key != int ):
                    xmin = k #Выдаем минимальное значение
                elif( type(k) == str ): #Если k является строкой, попытка проверить условия elif'а ниже вызовет ошибку
                    #т.к. str не конвертируется в int
                    continue #Данный elif помогает избежать этой ошибки
                elif( (int(k) < int(xmin)) and key == int ):
                    xmin = k #Учитывая ключ, выдаем первое минимальное значение в массиве
            print(f'Min = {xmin}')
    #Проверка на кол-во аргументов
    if(len(arg) == 1): #Если аргумент один
        iter(arg[0]) #Проверка на итерируемость одиночного аргумента
        innermin(arg[0])
    else: #Если аргументов больше одного
        innermin(arg)

def max(*arg, key=''):
    def innermax(inarg): #Функция, написанная внутри функции во избежание дубликации кода
        #Определение дальнейших действий в зависимости от ключа
        if( callable(key) and (key != int) ): #Если ключ является функцией (lambda)
            xmax = key(inarg[0])
            kmax = inarg[0]
            for k in inarg:
                if(key(k) > xmax):
                    xmax = key(k)
                    kmax = k
            print(f'Max = {kmax}')
        else: #Если ключ является типом данных
            xmax = inarg[0]
            for k in inarg:
                if( (k > xmax) and key != int ):
                    xmax = k #Выдаем минимальное значение
                elif( type(k) == str ): #Если k является строкой, попытка проверить условия elif'а ниже вызовет ошибку
                    #т.к. str не конвертируется в int
                    continue #Данный elif помогает избежать этой ошибки
                elif( (int(k) > int(xmax)) and key == int ):
                    xmax = k #Учитывая ключ, выдаем первое минимальное значение в массиве
            print(f'Max = {xmax}')
    #Проверка на кол-во аргументов
    if(len(arg) == 1): #Если аргумент один
        iter(arg[0]) #Проверка на итерируемость одиночного аргумента
        innermax(arg[0])
    else: #Если аргументов больше одного
        innermax(arg)

min(3, 2)
min( [3.3, 2.5, 2.3, 4.4] )
min( [3.3, 2.5, 2.3, 4.4], key=int )
min('hello')
min( [ [1, 2], [9, 0], [3, 4] ], key=lambda x: x[1] )
print('-----')
max(3, 2)
max( [3.3, 4.1, 2.3, 4.4] )
max( [3.3, 4.1, 2.3, 4.4], key=int )
max('Hello')
max( [ [1, 2], [3, 4], [9, 0] ], key=lambda x: x[1] )
