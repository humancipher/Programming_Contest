N = int(input())
a = []
for i in range(N):
	a.append(int(input()))

b = sorted(a)
max1 = b[N-1]
max2 = b[N-2]

if max1==max2:
	for i in range(N):
		print(max1)
else:
	for i in range(N):
		if a[i]==max1:
			print(max2)
		else:
			print(max1)
