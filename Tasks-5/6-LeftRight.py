tekst = ["alright", "bright", "left", "ok"]

for k in range(len(tekst)):
    tmp = tekst[k]
    for i in range(len(tekst[k])-4):
        if(tekst[k][i] == 'r' and tekst[k][i+1] == 'i' and tekst[k][i+2] == 'g' and tekst[k][i+3] == 'h' and tekst[k][i+4] == 't'):
            tekst[k] = tekst[k].removesuffix('right')
            tekst[k] += 'left'

for k in tekst:
    print(k)