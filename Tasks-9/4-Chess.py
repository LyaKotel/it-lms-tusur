coords = ["b4", "c4", "d4", "e4", "f4", "g4", "e5"]
#coords = ['a8', 'c8', 'd8', 'b7', 'c7'] #3 защищенных пешки
tmp = []
safe = 0

for k in range(len(coords)):
    tmp.append(list(coords[k]))
    tmp[k] = [ord(tmp[k][0]), int(tmp[k][1])]

for k, i in tmp:
    #print(k , i)
    if( ([k-1, i-1] in tmp) or ([k+1, i-1] in tmp) ):
        safe += 1

print(f'Защищенных пешек: {safe}')