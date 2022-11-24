num = 10

def CheckNum(x):
    if(x % 2 != 0):
        print("Плохо")
        return
    if( 2 <= x <= 5 and x % 2 == 0):
        print("Неплохо")
        return
    if( 6 <= x <= 20 and x % 2 == 0):
        print("Так себе")
        return
    if(x > 20 and x % 2 == 0):
        print("Отлично")
        return

CheckNum(num)