elem = [1,2,3,4]
elem = sorted(elem)
print(elem)

if(len(elem)%2 == 0):
    tmp = (elem[len(elem)//2 - 1] + elem[len(elem)//2])/2
    print(tmp)
else:
    print(elem[len(elem)//2])