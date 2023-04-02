from statistics import mean

#Класс студентов
class Student:
    #Конструктор
    def __init__(self, name, surname, physic, math, history, phys_edu):
        self.name = name
        self.surname = surname
        #print(f'Сработал Student конструктор "{self.name} {self.surname}"')
        self.marklist = {'physic':physic, 
                        'math':math, 
                        'history':history, 
                        'phys_edu':phys_edu}
    #Средний балл студента
    def midmark(self):
        midmark = mean(list(self.marklist.values()))
        print(f'Средний балл студента "{self.name} {self.surname}":', midmark)
        return midmark

#Класс групп
class Group:
    #Конструктор
    def __init__(self, groupnum, *students):
        self.groupnum = groupnum
        self.students = students
        #print(f'Сработал Group "{self.groupnum}" конструктор')
    #Средний балл группы
    def grmidmark(self):
        st_midmarks = []
        for k in self.students:
            st_midmarks.append( k.midmark()) 
        grmidmark = mean(st_midmarks)
        print(f'Средний балл группы {self.groupnum}:', grmidmark)
        return grmidmark
    #Средний балл по конкретному предмету
    def lesson_midmark(self, chosed_lesson):
        st_lesson_marks = []
        for k in self.students:
            st_lesson_marks.append(k.marklist[chosed_lesson])
        lesson_midmark = mean(st_lesson_marks)
        print(f'Средний балл группы {self.groupnum} по предмету "{chosed_lesson}":', lesson_midmark)
        return lesson_midmark

st = Student('Тест', 'Тестовый', 2, 3, 4, 5)
st.midmark()

g307 = Group('307', 
            Student('Иван', 'Иванов', 3, 3, 4, 5),
            Student('Алена', 'Жмильева', 5, 4, 4, 3),
            Student('Валерий', 'Денисов', 4, 3, 5, 3),
            Student('Олег', 'Змееносцев', 2, 3, 2, 3),
            Student('Ольга', 'Капустова', 4, 3, 2, 4) )
g307.grmidmark()
g307.lesson_midmark('history')

print('-----------')

g183 = Group('183',
            Student('Николай', 'Басин', 4, 4, 5, 5),
            Student('Светлана', 'Темнова', 3, 3, 5, 4),
            Student('Артем', 'Витых', 5, 5, 3, 2) )
g183.grmidmark()
g183.lesson_midmark('physic')