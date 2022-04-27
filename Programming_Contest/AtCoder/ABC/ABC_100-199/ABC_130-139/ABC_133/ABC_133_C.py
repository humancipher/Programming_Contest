Line = list(map(int, input().split(" ")))
L = Line[0]
R = Line[1]

min=2018
if L//2019 != R//2019 or L%2019==0 or R%2019==0:
	print(0)
else:
	for i in range(L,R+1):
		for j in range(i+1,R+1):
			if ((i%2019)*(j%2019))%2019<min:
				min=((i%2019)*(j%2019))%2019
	print(min)
