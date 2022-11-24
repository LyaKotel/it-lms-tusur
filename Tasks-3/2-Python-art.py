#Рисует букву Н с заданными параметрами ширины и высоты
width = 5
height = 7
schedule = 'H'
space = ' '

#Т.к. верхняя и нижняя части буквы Н идентичны, объявим функцию
def HLegs():
    for k in range(height):
        tmp = schedule*width + space*width + schedule*width
        print(tmp)

#Верхняя часть буквы Н
HLegs()

#Средняя часть буквы Н
for k in range(height):
    print(schedule*width*3)

#Нижняя часть буквы Н
HLegs()