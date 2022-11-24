import numpy as np

result = []
encrypted = (('X...',
              '..X.',
              'X..X',
              '....'),
            ('itdf',
             'gdce',
             'aton',
             'qrdi'))

#Извлечение данных из кортежа
codekey = [[encrypted[0][i][k] for k in range(len(encrypted[0]))] for i in range(len(encrypted[0]))]
letters = [[encrypted[1][i][k] for k in range(len(encrypted[1]))] for i in range(len(encrypted[1]))]

#Расшифровка сообщения
for j in range(4): #4 раза т.к. мы заранее знаем, что решетку надо повернуть ровно 4 раза
    #Сопоставление букв и меток на решетке
    for k in range(len(letters)):
        for i in range(len(letters)):
            if(codekey[k][i] == 'X'):
                result += letters[k][i]
    codekey = np.rot90(codekey, k = -1)

print(''.join(result))