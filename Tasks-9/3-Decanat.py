from collections import OrderedDict
from statistics import mean

studlist = OrderedDict({ 
    1:{
    'Фамилия':'Иванов',
    'Имя':'Иван',
    'Отчество':'Иванович',
    'Год':1999,
    'Курс':1,
    'Группа':777,
    'Оценки':[5, 5, 4, 3, 2]
    },
    2:{
    'Фамилия':'Зубенко',
    'Имя':'Михаил',
    'Отчество':'Петрович',
    'Год':1990,
    'Курс':3,
    'Группа':227,
    'Оценки':[2, 2, 2, 2, 2]
    },
    3:{
    'Фамилия':'Маск',
    'Имя':'Илон',
    'Отчество':'Теслович',
    'Год':2077,
    'Курс':5,
    'Группа':777,
    'Оценки':[5, 5, 5, 5, 5]
    },
    4:{
    'Фамилия':'Несуществующий',
    'Имя':'Олег',
    'Отчество':'Артемович',
    'Год':1990,
    'Курс':3,
    'Группа':227,
    'Оценки':[3, 3, 5, 4, 3]
    },
    5:{
    'Фамилия':'Йогуртов',
    'Имя':'Данил',
    'Отчество':'Никитович',
    'Год':2001,
    'Курс':3,
    'Группа':227,
    'Оценки':[4, 4, 4, 2, 3]
    }
})

#Сортировка студентов по курсу
def sortkurs():
    tmp = []
    #Извлечение необходимых данных о студентах
    for k in range(1, len(studlist)+1):
        tmp.append( [ studlist[k]['Фамилия'], studlist[k]['Имя'], studlist[k]['Отчество'], studlist[k]['Курс'] ] )
    #Сортировка студентов
    for k in range(len(tmp)):
        for i in range(len(tmp)-1):
            if( tmp[i][3] > tmp[i+1][3] ):
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
            #Т.к. условия сортировки студентов являются не совсем стандартными
            #(не просто по номеру курса, а еще и с учетом алфавитного порядка), 
            #то и стандартные функции сортировки здесь не подойдут, поэтому был 
            #написан алгоритм сортировки пузырьком с учетом наших условий
            elif( (ascii(tmp[i][0][0]) > ascii(tmp[i+1][0][0])) and (tmp[i][3] == tmp[i+1][3]) ):
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]

    print('Список студентов:')
    for k in range(len(tmp)):
        print(tmp[k])

#Средние оценки по группе
def midmark():
    marks = {} #Здесь производится суммирование всех оценок группы по каждому предмету
    students = {} #Здесь ведется подсчет количества студентов в группе, чтобы в конце получить среднее значение
    mid = []
    #Здесь сумма всех оценок группы по каждому предмету
    for k in range(1, len(studlist)+1):
        if(studlist[k]['Группа'] in marks):
            students[studlist[k]['Группа']] += 1
            for i in range(len(marks[studlist[k]['Группа']])):
                marks[studlist[k]['Группа']][i] += studlist[k]['Оценки'][i]
        else:
            marks[studlist[k]['Группа']] = [0, 0, 0, 0, 0]
            students[studlist[k]['Группа']] = 1
            for i in range(len(marks[studlist[k]['Группа']])):
                marks[studlist[k]['Группа']][i] += studlist[k]['Оценки'][i]
    #Здесь из вышеописанной суммы оценок получаются средние значения, далее идет запись в массив на print()
    for key, val in marks.items():
        print(f'Средние оценки группы {key}:')
        for i in val:
            mid.append(round(i/students[key], 2)) #Сумма по одному конкретному предмету делится на кол-во студентов в группе
        print(mid)
        mid = []

#Нахождение самого старшего/младшего студента
def oldyoungstud():
    agemax = agemin = studlist[1]['Год'] #В качестве начального значения берется первое значение в словаре
    for k in range(1, len(studlist)+1):
        #Сравнивается год рождения студента из studlist с переменными agemax, agemin.
        #Самый младший/старший студент записывается в studyoung и studold соответственно
        if( studlist[k]['Год'] < agemin ):
            agemin = studlist[k]['Год']
            studold = [studlist[k]['Фамилия'], studlist[k]['Имя'], studlist[k]['Отчество'], studlist[k]['Год']]
        if( studlist[k]['Год'] > agemax ):
            agemax = studlist[k]['Год']
            studyoung = [studlist[k]['Фамилия'], studlist[k]['Имя'], studlist[k]['Отчество'], studlist[k]['Год']]
    print(f'Самый старший студент: {studold}')
    print(f'Самый младший студент: {studyoung}')

#Определение лучшего студента в группе
def beststudent():
    tmp = {}
    bestmark = {}
    beststud = {}
    #Предварительно создаем ключ с пустым маасивом значением для каждой группы
    for key, val in studlist.items():
        tmp[val['Группа']] = []

    #Записываем студентов в соотвествии с группами вместе с их средними баллами по зачетке
    #в словарь записывается только ФИО и средний балл
    for k in range(1, len(studlist)+1):
            tmp[studlist[k]['Группа']].append([studlist[k]['Фамилия'], studlist[k]['Имя'], studlist[k]['Отчество'], round(mean(studlist[k]['Оценки']))])

    #Лпределение лучшего студента в каждой группе
    for key, val in tmp.items():
        bestmark[key] = 0
        for k in val:
            if( k[3] > bestmark[key] ):
                bestmark[key] = k[3]
                beststud[key] = k
    
    for key, val in beststud.items():
        print(f'Лучший студент в группе {key} - {beststud[key][0]} {beststud[key][1]} {beststud[key][2]}(Средний балл по зачетке: {beststud[key][3]})')

        
#sortkurs()
#midmark()
#oldyoungstud()
beststudent()