line = list(map(int, input().split(" ")))

A=line[0]
B=line[1]
C=line[2]

if B+C>=A:
	print(B+C-A)
else:
	print(0)
