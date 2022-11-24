def main():
    #Т.к. возраст привидений не уходит в бесконечность и не превышает 5000 лет, запишем числа Фибоначчи в список
    FibonachiNum = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    start_visibility = 10000 #Значение прозрачности, с которого мы начинаем счет
    stop_visibility = 9990 #Значение прозрачности, на котором нам следует остановиться
    age = 0

    #Если привидению 0 лет
    if(stop_visibility == 10000):
        print('Возраст: 0')
        return
    
    #Определение возраста привидения
    while( (start_visibility != stop_visibility) and (age <= 5000) ):
        age += 1
        if(age in FibonachiNum):
            start_visibility -= age
        else:
            start_visibility += 1
    
    if(age > 5000):
        print('Привидение давно исчезло. Возраст больше 5000 тысяч лет')
    else:
        print(f'Возраст: {age}')
    return

if(__name__ == '__main__'):
    main()