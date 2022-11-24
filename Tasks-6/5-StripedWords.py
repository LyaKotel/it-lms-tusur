glasnieHigh = ["A", "E", "I", "O", "U", "Y"]
glasnieLow = ["a", "e", "i", "o", "u", "y"]
glasnie = glasnieLow + glasnieHigh

soglasnieHigh = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
soglasnieLow = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
soglasnie = soglasnieLow + soglasnieHigh

strmarks = '''!()-[]}{;?@#$%:'"\,./^&;*_'''
count = 0
BreakFlag = False

text = "Dog,cat,mouse,bird.Human."

text = list(text)
for k in range(len(text)):
    if (text[k] in strmarks):
        text[k] = " "

text = "".join(text)
tmptext = text.split()

for k in range(len(tmptext)):

    word = list(tmptext[k])

    if(len(word) != 1):
        for i in range(len(word)-1):
            if(not((word[i] in glasnie) and (word[i+1] in soglasnie) or (word[i] in soglasnie) and (word[i+1] in glasnie))):
                BreakFlag = True
        if(BreakFlag == False): 
            count += 1
            print(word, " - True")
        BreakFlag = False

print(count)