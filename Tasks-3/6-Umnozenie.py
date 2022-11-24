num = 234
mult = 1

while (num != 0):
    tmp = num % 10
    if(tmp != 0):
        mult = mult * tmp
    num = num // 10
print("Произведение: ", mult)