num = int(input())
l=[]
for i in range(1,num+1):
	if(num%i==0):
		l.append(i)
if(len(l)==2):
	print(num, 'is a prime number')
else:
	print(num, " Is Not a prime Number")
