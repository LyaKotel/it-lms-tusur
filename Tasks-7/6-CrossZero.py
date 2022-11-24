def main():
    data = ["OOX", 
            "XXO", 
            "OXX"]

    matrix = (list(data[0]), list(data[1]), list(data[2]))
    tmp = ''

    for i in range(3):
        for k in range(3):
            tmp += matrix[i][k]
        if(tmp == 'XXX'):
            print('X')
            return
        elif(tmp == 'OOO'):
            print('O')
            return
        tmp = ''

    tmp = ''

    for i in range(3):
        for k in range(3):
            tmp += matrix[k][i]
        if(tmp == 'XXX'):
            print('X')
            return
        elif(tmp == 'OOO'):
            print('O')
            return
        tmp = ''

    print('D')
    return

if(__name__ == '__main__'):
    main()