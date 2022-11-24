num = 89162
revnum = ''

print("num = ", num)

while(num != 0):
	tmp = num % 10
	num = num // 10
	revnum = revnum + str(tmp)	

print("revnum = ", revnum)