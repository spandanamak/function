def fun(n):
	if n==0:
		return 1
	else:
		return n*fun(n-1)
n=int(input('enter the number'))
b=fun(n)
print(b)
