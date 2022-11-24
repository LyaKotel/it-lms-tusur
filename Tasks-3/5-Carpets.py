width = 11
length = width*3
num = 1 #Число для построения узора в верхней и нижней части ковра

#Верхняя часть ковра
for k in range(width-int(width/2)):
    tmp = '0'*int(width/2-k) + '#'*num + '0'*int(width/2-k)
    num += 2
    print(tmp)

k += 1 #Прибавляем единицу, как если бы мы вели счет от единицы, а не от нуля
midpart = length-k*2 #Вычисление середины ковра

#Средняя часть ковра
for k in range(midpart):
    if(k == int(midpart/2)):
        tmp = '-'*int((width-7)/2) + 'WELCOME' + '-'*int((width-7)/2)
        print(tmp)
    else:
        print('H'*width)

#Нижняя часть ковра
for k in range(width-int(width/2)):
    tmp = '0'*k + '#'*(width-k*2) + '0'*k
    print(tmp)