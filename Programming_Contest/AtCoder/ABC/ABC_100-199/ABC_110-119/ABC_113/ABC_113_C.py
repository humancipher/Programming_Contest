def pad(n):
	n = str(n)
	if len(n) < 6:
		n = "0"*(6-len(n))+n
	return n

N,M = map(int,input().split())
PY = [list(map(int,input().split())) for _ in range(M)]

for i in range(M):
	PY[i].append(i)
PY.sort()

turn = 1
PY[0].append(pad(PY[0][0])+pad(turn))
for i in range(1,M):
	if PY[i][0] != PY[i-1][0]:
		turn = 1
	else:
		turn += 1
	PY[i].append(pad(PY[i][0])+pad(turn))

PY.sort(key = lambda x:x[2])
for i in range(M):
	print(PY[i][3])
