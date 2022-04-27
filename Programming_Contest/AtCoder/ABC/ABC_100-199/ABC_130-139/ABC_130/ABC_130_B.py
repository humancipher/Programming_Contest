#python ABC_130_B.py

line1 = list(map(int, input().split(" ")))
L = list(map(int, input().split(" ")))

N = line1[0]
X = line1[1]

D = 0
count = 1

for i in range(N):
	D = D + L[i]
	if D<=X:
		count = count + 1

print(count)
