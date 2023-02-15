def foo(n):
    for k in range(n+1):
        if(k == 0):
            yield -10
        elif(k % 3):
            yield 45
        elif(k % 5):
            yield (k / 5) + 93
        else:
            yield k/2

print(list(foo(3)))