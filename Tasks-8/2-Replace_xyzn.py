tmpx = tmpy = tmpz = 0
x = y = z = 1
n = 2

result = [[tmpx, tmpy, tmpz]
          for tmpx in range(x + 1)
          for tmpy in range(y + 1)
          for tmpz in range(z + 1)
          if(tmpx + tmpy + tmpz != n)]

print(result)