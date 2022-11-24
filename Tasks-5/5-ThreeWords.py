tekst = '11 11 ff aa ss 88 ss 00'

def ThreeWords(tekst):
    tmp = tekst.split()
    for k in range(len(tmp) - 2):
        print("k = ",k)
        print("k+1 = ",k+1)
        print("k+2 = ",k+2)
        print("-----")
        if(tmp[k].isalpha() and tmp[k+1].isalpha() and tmp[k+2].isalpha()):
            print("True")
            return
    print("False")

ThreeWords(tekst)