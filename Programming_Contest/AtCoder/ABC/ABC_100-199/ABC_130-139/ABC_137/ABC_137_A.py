a = list(map(int, input().split(" ")))
A=a[0]
B=a[1]

if A+B>=A-B and A+B>=A*B:
	print(A+B)
elif A-B>=A+B and A-B>=A*B:
	print(A-B)
else:
	print(A*B)
