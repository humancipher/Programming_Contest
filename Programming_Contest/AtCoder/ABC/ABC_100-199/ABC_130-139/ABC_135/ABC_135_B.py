N = int(input())
p = list(map(int, input().split(" ")))
q = [i for i in range(1,N+1)]

count = 0
for i in range(N):
	if p[i]!=q[i]:
		count += 1
if count == 0 or count == 2:
	print('YES')
else:
	print('NO')
