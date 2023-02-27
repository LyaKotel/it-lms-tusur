def randuniform(n):
    from random import uniform
    return list( (uniform(0, n) for k in range(n)) )

print(randuniform(5))