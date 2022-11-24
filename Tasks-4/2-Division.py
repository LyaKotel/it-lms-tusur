import random as rd

num1 = rd.randint(100,300)
num2 = rd.randint(10,50)

result = int(num1/num2)
ostatok = num1%num2

print("Первое число: ", num1)
print("Второе число: ", num2)

print("Разность: ", result)
print("Остаток: ", ostatok)