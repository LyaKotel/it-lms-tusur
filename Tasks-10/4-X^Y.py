def main():
    num = [2, 3 ,4]
    degree = [5, 3, 2,]

    if(len(num) != len(degree)):
        print('Error. Different lenth')
        return

    result = [num[k]**degree[k] for k in range(len(num))]
    print(result)

if(__name__ == '__main__'):
    main()