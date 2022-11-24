num = 123 #999000555111 
revnum = ''

print("num = ", num)

while(num != 0):
	tmp = num % 10
	num = num // 10
	revnum = revnum + str(tmp)	

if (-2147483648 <= int(revnum) <= 2147483647):
    print("revnum = ", revnum)
else:
    print("revnum = 0")


