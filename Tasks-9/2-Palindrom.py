from string import ascii_lowercase

def Palindrome(fstr):
    #Проверка на прописную латиницу без цифр
    for k in fstr:
        if(k not in ascii_lowercase):
            print(fstr, '-> Error. String contains upper register or numbers')
            return
    #Проверка на палиндром
    revfstr = fstr
    revfstr = fstr[::-1]
    if(fstr == revfstr):
        print(fstr, '-> True')
    else:
        print(fstr, '-> False')
    

Palindrome('tacocat')
Palindrome('lol')
Palindrome('palindrome')
Palindrome('123ItDoesntWork')