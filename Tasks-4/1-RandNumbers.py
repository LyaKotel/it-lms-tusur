import random as rd

num1 = rd.randint(0,100)
num2 = rd.randint(0,50)
num3 = rd.randint(0,200)

print("Первое число: ", num1)
print("Второе число: ", num2)
print("Третье число: ", num3)

midarif = (num1 + num2 + num3)/3
print("Среднее арифметическое: {0:.2f}".format(midarif))