from collections import OrderedDict
romedir = OrderedDict()
romedir['M'] = 1000
romedir['CM'] = 900
romedir['D'] = 500
romedir['CD'] = 400
romedir['C'] = 100
romedir['XC'] = 90
romedir['L'] = 50
romedir['XL'] = 40
romedir['X'] = 10
romedir['IX'] = 9
romedir['V'] = 5
romedir['IV'] = 4
romedir['I'] = 1

num = 3999
rome = ''

while(num > 0):
    for key, val in romedir.items():
        if(num >= val):
            rome += key
            num -= val
            break

print(rome)