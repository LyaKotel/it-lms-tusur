text = "hello, word of word"
strmarks = '''!()-[]}{;?@#$%:'"1234567890\,./^&;*_'''
total_letters = {}
total_words = {}

#Разбиваем строку на символы
letters = list(text)
#Обработка символов
for k in range(len(letters)):
    #Очистка от посторонних знаков
    if(letters[k] in strmarks):
        letters[k] = " "
    #Подсчет символов
    if(letters[k] not in total_letters and letters[k] != " "):
        total_letters[letters[k]] = 1
    elif(letters[k] in total_letters):
        total_letters[letters[k]] += 1
    #################
#print(letters)
print(total_letters)

#Составление слов из букв
tmpwords = "".join(letters)
words = tmpwords.split()
#Подсчет слов
for k in range(len(words)):
    if(words[k] in total_words):
        total_words[words[k]] += 1
    else:
        total_words[words[k]] = 1
###############
#print(words)
print(total_words)