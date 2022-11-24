tekst = 'Когда загорится Огонь, я буду действовать в полную силу, потому что День на моей стороне'
tmp = ''

for k in tekst:
    if(k.isupper()):
        tmp = tmp + k

print(tmp)