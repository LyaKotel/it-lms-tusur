elem = [1,2,3,4,5,6,7,8,9]

if(len(elem) == 0):
    print(0)
else:
    tmp = elem[::2]
    result = sum(tmp) * elem[-1]
    print(result)