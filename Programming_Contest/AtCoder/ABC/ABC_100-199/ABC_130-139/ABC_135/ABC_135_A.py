line = list(map(int, input().split(" ")))
A = line[0]
B = line[1]

if (A+B)%2==0:
	print(int((A+B)/2))
else:
	print('IMPOSSIBLE')
