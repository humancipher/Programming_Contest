line = list(map(int, input().split(" ")))
N = line[0]
L = line[1]
sum = 0
for i in range(N):
	sum = sum + L+i

if L>=0:
	print(sum-L)
elif L+N-1<=0:
	print(sum-(L+N-1))
else:
	print(sum)
