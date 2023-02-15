sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = (x.count('капитан') for x in sentences)

print(sum(cap_count))